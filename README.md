# ✅ Task Manager — FastAPI + Vanilla JS

A full-stack Task Manager application with JWT authentication, built as part of a Python Developer Intern assignment.

## 🚀 Live Demo

> _Add your deployment URL here after deploying_

## 🧱 Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | FastAPI, SQLAlchemy, SQLite        |
| Auth      | JWT (python-jose), bcrypt          |
| Frontend  | Vanilla HTML + CSS + JavaScript    |
| Testing   | pytest, httpx                      |
| Deploy    | Render / Railway (Docker)          |

---

## 📁 Project Structure

```
task-manager/
├── backend/
│   ├── app/
│   │   ├── core/         # config, security (JWT, hashing)
│   │   ├── db/           # SQLAlchemy engine + session
│   │   ├── models/       # ORM models (User, Task)
│   │   ├── routers/      # auth.py, tasks.py
│   │   ├── schemas/      # Pydantic schemas
│   │   └── main.py       # FastAPI app entry point
│   ├── tests/
│   │   └── test_api.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── index.html        # Single-page frontend
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` inside the `backend/` folder and fill in:

```env
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./taskmanager.db
```

> ⚠️ **Never commit `.env` to version control.**

---

## 🖥️ Running Locally

### Option 1 — Direct (Python)

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd task-manager/backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your values

# 5. Run the server
uvicorn app.main:app --reload
```

The app will be available at **http://localhost:8000**  
API docs: **http://localhost:8000/docs**

### Option 2 — Docker

```bash
docker-compose up --build
```

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

---

## 📡 API Endpoints

### Auth

| Method | Endpoint    | Description         |
|--------|-------------|---------------------|
| POST   | `/register` | Register a new user |
| POST   | `/login`    | Login, get JWT      |

### Tasks (🔒 Authenticated)

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| POST   | `/tasks`         | Create a task                    |
| GET    | `/tasks`         | List tasks (paginated + filter)  |
| GET    | `/tasks/{id}`    | Get a specific task              |
| PUT    | `/tasks/{id}`    | Update a task                    |
| DELETE | `/tasks/{id}`    | Delete a task                    |

**Query params for `GET /tasks`:**
- `?completed=true` / `?completed=false` — filter by status
- `?page=1&page_size=10` — pagination

---

## 🌐 Deploying to Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r backend/requirements.txt`
   - **Start Command:** `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables from `.env.example`
6. Deploy!

---

## ✅ Features

- [x] User registration & login
- [x] JWT-based authentication
- [x] Password hashing with bcrypt
- [x] Full task CRUD
- [x] Users can only access their own tasks
- [x] Pagination (`page`, `page_size`)
- [x] Filtering by completion status
- [x] Clean folder structure
- [x] Pydantic v2 schemas
- [x] Proper HTTP status codes & error handling
- [x] pytest test suite (12 tests)
- [x] Dockerfile + docker-compose
- [x] Responsive single-page frontend
- [x] `/docs` Swagger UI accessible
