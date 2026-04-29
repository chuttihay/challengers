# 🚀 Backend (FastAPI) & Database (PostgreSQL) Setup Guide

This guide helps new contributors set up the **FastAPI backend** and **PostgreSQL database** for this project.

---

# 🧠 Backend – FastAPI Setup

## 📦 Prerequisites

Make sure you have installed:

* Python 3.10+ (recommended 3.11)
* pip
* virtualenv (optional but recommended)
* PostgreSQL running locally or via Docker

---

## 📁 Project Structure

```
backend/
  app/
    main.py
    api/
    models/
    services/
    db/
  requirements.txt
  .env.example
```

---

## ⚙️ Setup Instructions

### 1. Navigate to backend

```bash
cd backend
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt does not exist yet, initialize FastAPI dependencies:

```bash
pip install fastapi uvicorn psycopg2-binary sqlalchemy python-dotenv
pip freeze > requirements.txt
```

---

### 4. Environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
ENV=development
```

---

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

API docs:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Basic FastAPI Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running"}
```

---

## 🧱 Common Commands

Run server:

```bash
uvicorn app.main:app --reload
```

Install new dependency:

```bash
pip install package-name
pip freeze > requirements.txt
```
