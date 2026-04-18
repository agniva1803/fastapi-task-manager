import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import Base, get_db

TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def register_and_login(username="testuser", email="test@example.com", password="secret123"):
    client.post("/register", json={"username": username, "email": email, "password": password})
    resp = client.post("/login", data={"username": username, "password": password})
    return resp.json()["access_token"]


def auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_register_success():
    resp = client.post("/register", json={"username": "alice", "email": "alice@example.com", "password": "pw123"})
    assert resp.status_code == 201
    assert resp.json()["username"] == "alice"


def test_register_duplicate_username():
    client.post("/register", json={"username": "bob", "email": "bob@example.com", "password": "pw"})
    resp = client.post("/register", json={"username": "bob", "email": "bob2@example.com", "password": "pw"})
    assert resp.status_code == 400


def test_register_duplicate_email():
    client.post("/register", json={"username": "carol", "email": "carol@example.com", "password": "pw"})
    resp = client.post("/register", json={"username": "carol2", "email": "carol@example.com", "password": "pw"})
    assert resp.status_code == 400


def test_login_success():
    client.post("/register", json={"username": "dave", "email": "dave@example.com", "password": "mypass"})
    resp = client.post("/login", data={"username": "dave", "password": "mypass"})
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_wrong_password():
    client.post("/register", json={"username": "eve", "email": "eve@example.com", "password": "correct"})
    resp = client.post("/login", data={"username": "eve", "password": "wrong"})
    assert resp.status_code == 401


def test_create_task():
    token = register_and_login()
    resp = client.post("/tasks", json={"title": "Buy milk", "description": "2% please"}, headers=auth(token))
    assert resp.status_code == 201
    assert resp.json()["title"] == "Buy milk"
    assert resp.json()["completed"] is False


def test_get_all_tasks():
    token = register_and_login()
    h = auth(token)
    client.post("/tasks", json={"title": "Task A"}, headers=h)
    client.post("/tasks", json={"title": "Task B"}, headers=h)
    resp = client.get("/tasks", headers=h)
    assert resp.status_code == 200
    assert resp.json()["total"] == 2


def test_get_task_by_id():
    token = register_and_login()
    created = client.post("/tasks", json={"title": "Specific"}, headers=auth(token)).json()
    resp = client.get(f"/tasks/{created['id']}", headers=auth(token))
    assert resp.status_code == 200
    assert resp.json()["title"] == "Specific"


def test_get_task_not_found():
    token = register_and_login()
    assert client.get("/tasks/9999", headers=auth(token)).status_code == 404


def test_mark_task_completed():
    token = register_and_login()
    task = client.post("/tasks", json={"title": "Finish report"}, headers=auth(token)).json()
    resp = client.put(f"/tasks/{task['id']}", json={"completed": True}, headers=auth(token))
    assert resp.status_code == 200
    assert resp.json()["completed"] is True


def test_delete_task():
    token = register_and_login()
    task = client.post("/tasks", json={"title": "Temp task"}, headers=auth(token)).json()
    assert client.delete(f"/tasks/{task['id']}", headers=auth(token)).status_code == 204
    assert client.get(f"/tasks/{task['id']}", headers=auth(token)).status_code == 404


def test_filter_tasks_by_completed():
    token = register_and_login()
    h = auth(token)
    t1 = client.post("/tasks", json={"title": "Done"}, headers=h).json()
    client.post("/tasks", json={"title": "Not done"}, headers=h)
    client.put(f"/tasks/{t1['id']}", json={"completed": True}, headers=h)
    assert client.get("/tasks?completed=true", headers=h).json()["total"] == 1
    assert client.get("/tasks?completed=false", headers=h).json()["total"] == 1


def test_user_cannot_access_other_users_tasks():
    t1 = register_and_login("user1", "u1@test.com", "pass1")
    t2 = register_and_login("user2", "u2@test.com", "pass2")
    task = client.post("/tasks", json={"title": "Private"}, headers=auth(t1)).json()
    assert client.get(f"/tasks/{task['id']}", headers=auth(t2)).status_code == 404


def test_pagination():
    token = register_and_login()
    h = auth(token)
    for i in range(15):
        client.post("/tasks", json={"title": f"Task {i}"}, headers=h)
    p1 = client.get("/tasks?page=1&page_size=10", headers=h).json()
    p2 = client.get("/tasks?page=2&page_size=10", headers=h).json()
    assert len(p1["tasks"]) == 10
    assert len(p2["tasks"]) == 5
    assert p1["total"] == 15


def test_unauthorized_access():
    assert client.get("/tasks").status_code == 401
