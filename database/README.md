# 🗄️ Database – PostgreSQL Setup

## 📦 Prerequisites

* PostgreSQL installed locally OR Docker
* psql CLI (optional but helpful)

---

## ⚙️ Local PostgreSQL Setup

### 1. Create database

```bash
psql postgres
```

Then inside psql:

```sql
CREATE DATABASE myapp_db;
CREATE USER myapp_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myapp_db TO myapp_user;
```

---

## 🐳 Docker Option (Recommended)

Run PostgreSQL via Docker:

```bash
docker run --name postgres-db \
  -e POSTGRES_USER=myapp_user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=myapp_db \
  -p 5432:5432 \
  -d postgres
```

---

## 🔌 Connection String

Use this format in your `.env`:

```env
DATABASE_URL=postgresql://myapp_user:password@localhost:5432/myapp_db
```

---

## 🧱 Suggested Database Folder Structure

```
database/
  schema.sql
  migrations/
  seeds/
  README.md
```

---

## 📄 Example schema.sql

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🧪 Testing DB Connection (FastAPI)

```python
from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    print(result.fetchone())
```

---

# 🔁 Recommended Workflow

1. Start PostgreSQL
2. Run FastAPI server
3. Connect backend → database via `.env`
4. Call API from Flutter frontend

---

# 🚀 Next Steps

Recommended improvements:

* Add Alembic migrations
* Add Docker Compose (backend + db)
* Add authentication (JWT)
* Add CI pipeline for backend tests

---

Happy building ⚡
