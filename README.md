# 🀝 FastAPI Task Manager

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite)](https://sqlite.org)
[![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=flat-square)](https://jwt.io)

> A production-grade task management REST API with JWT authentication, persistent SQLite storage, and a vanilla JS frontend.

---

## ✨ Features

- βœ… **Full CRUD** β€" Create, read, update, delete tasks
- πŸ"' **JWT Authentication** β€" Secure register/login flow
- πŸ'Ύ **SQLite Persistence** β€" Tasks survive server restarts
- πŸ"– **Auto Docs** β€" Swagger UI at `/docs`, ReDoc at `/redoc`
- πŸ–₯️ **Vanilla JS Frontend** β€" No framework, pure HTML/CSS/JS
- ⚑ **FastAPI** β€" Async endpoints, type-safe with Pydantic

---

## πŸš€ Quick Start

```bash
git clone https://github.com/agniva1803/fastapi-task-manager.git
cd fastapi-task-manager
pip install -r requirements.txt
uvicorn main:app --reload
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## πŸ"' API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/register` | ❌ | Register user |
| POST | `/auth/login` | ❌ | Login, get JWT |
| GET | `/tasks` | βœ… | List all tasks |
| POST | `/tasks` | βœ… | Create task |
| PUT | `/tasks/{id}` | βœ… | Update task |
| DELETE | `/tasks/{id}` | βœ… | Delete task |

---

## πŸ—οΈ Tech Stack

`Python` `FastAPI` `SQLite` `SQLAlchemy` `JWT` `Pydantic` `Uvicorn`

---

## πŸ'¨β€πŸ'» Author

**Agniva Mukherjee** β€" [GitHub](https://github.com/agniva1803) Β· [LinkedIn](https://www.linkedin.com/in/agniva-mukherjee-b2647b21a)

MIT Β© 2024 Agniva Mukherjee
