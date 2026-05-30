<div align="center">

# ⚡ FastAPI Task Manager

**Production-grade REST API with JWT authentication, persistent storage & vanilla JS frontend**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)](https://jwt.io)

</div>

---

## ✨ Features

- 🔐 **JWT Authentication** — secure register/login with token-based sessions
- ✅ **Full CRUD** — create, read, update, delete tasks
- 💾 **SQLite Persistence** — data survives restarts
- 🌐 **Vanilla JS Frontend** — zero dependencies, works in any browser
- 🐳 **Docker Ready** — one command to run
- 📖 **Auto API Docs** — Swagger UI at `/docs`
- ⚡ **FastAPI** — async Python, blazing fast

## 🚀 Quick Start

```bash
git clone https://github.com/agniva1803/fastapi-task-manager
cd fastapi-task-manager

# With Docker
docker-compose up

# Or manually
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://localhost:8000/docs` for the interactive API docs.

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | Python, FastAPI, Uvicorn |
| Auth | JWT (python-jose), bcrypt |
| Database | SQLite, SQLAlchemy |
| Frontend | HTML, CSS, Vanilla JS |
| DevOps | Docker, Docker Compose |

## 📁 Project Structure

```
fastapi-task-manager/
├── backend/
│   ├── main.py          # FastAPI app + routes
│   ├── models.py        # SQLAlchemy models
│   ├── auth.py          # JWT logic
│   └── requirements.txt
├── frontend/
│   └── index.html       # Vanilla JS frontend
└── Dockerfile
```

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/register` | ❌ | Register new user |
| POST | `/auth/login` | ❌ | Login, get JWT |
| GET | `/tasks` | ✅ | List all tasks |
| POST | `/tasks` | ✅ | Create task |
| PUT | `/tasks/{id}` | ✅ | Update task |
| DELETE | `/tasks/{id}` | ✅ | Delete task |

---

<div align="center">
Made by <a href="https://github.com/agniva1803">Agniva Mukherjee</a>
</div>
