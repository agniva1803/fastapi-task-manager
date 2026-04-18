# 📋 FastAPI Task Manager

A full-stack Task Manager application built with **FastAPI** (backend) and plain **HTML/CSS/JavaScript** (frontend).

## 🚀 Live Demo

**🌐 https://fastapi-task-manager-znn3.onrender.com**

- Frontend UI → https://fastapi-task-manager-znn3.onrender.com/
- API Docs    → https://fastapi-task-manager-znn3.onrender.com/docs

---

## ✨ Features

- **JWT Authentication** — register, login, secure token-based sessions
- **Task CRUD** — create, view, update, delete tasks
- **Mark as Complete** — toggle task completion status
- **Pagination** — `?page=1&page_size=10`
- **Filtering** — `?completed=true|false`
- **User isolation** — users can only access their own tasks
- **15 pytest tests** — all passing
- **Docker** ready

---

## 🏗️ Project Structure

```
task-manager/
├── backend/
│   ├── app/
│   │   ├── core/         # config.py, security.py
│   │   ├── db/           # database.py
│   │   ├── models/       # user.py, task.py (SQLAlchemy)
│   │   ├── routers/      # auth.py, tasks.py
│   │   ├── schemas/      # user.py, task.py (Pydantic)
│   │   └── main.py
│   ├── tests/
│   │   └── test_api.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── index.html
├── Dockerfile
└── README.md
```

---

## ⚙️ Environment Variables

```bash
cp backend/.env.example backend/.env
```

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | JWT signing secret — **change this!** | dev fallback |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime | `30` |
| `DATABASE_URL` | SQLAlchemy DB URL | `sqlite:///./taskmanager.db` |

> Never commit your `.env` file.

---

## 🖥️ Run Locally

```bash
git clone https://github.com/agniva1803/fastapi-task-manager.git
cd fastapi-task-manager/backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # set SECRET_KEY
uvicorn app.main:app --reload
```

### Run tests

```bash
cd backend
pytest tests/ -v
```

---

## 🐳 Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 -e SECRET_KEY=your-secret task-manager
```

---

## 📡 API Reference

### Auth
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/register` | Create account |
| `POST` | `/login` | Get JWT token |

### Tasks (Bearer token required)
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/tasks` | Create task |
| `GET` | `/tasks` | List tasks (paginated) |
| `GET` | `/tasks/{id}` | Get task |
| `PUT` | `/tasks/{id}` | Update task |
| `DELETE` | `/tasks/{id}` | Delete task |

Query params: `?completed=true/false`, `?page=1&page_size=10`

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

15 tests covering:
- User registration & login
- Duplicate username/email validation
- Full task CRUD
- Completion toggle
- Pagination
- Filtering by status
- User isolation (can't access other users' tasks)
- Unauthorized access protection

---

## 🚢 Deployed on Render

Live at: **https://fastapi-task-manager-znn3.onrender.com**

Deployed using [Render](https://render.com) with Docker. The `/docs` endpoint provides interactive Swagger UI for the API.
