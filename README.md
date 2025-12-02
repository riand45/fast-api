# FastAPI CRUD Application

A RESTful API for managing books using FastAPI, SQLModel, and PostgreSQL with async support.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Migrations](#database-migrations)
- [Development](#development)

## ✨ Features

- ✅ Full CRUD operations for Books
- ✅ Async/await support with asyncio
- ✅ PostgreSQL database with asyncpg driver
- ✅ SQLModel ORM for database operations
- ✅ Pydantic models for request/response validation
- ✅ Database migrations with Alembic
- ✅ Auto-generated API documentation (Swagger UI)
- ✅ Type hints throughout the codebase

## 🛠 Tech Stack

- **FastAPI** (0.122.0) - Modern web framework for building APIs
- **SQLModel** (0.0.27) - SQL database library based on SQLAlchemy and Pydantic
- **PostgreSQL** - Relational database
- **asyncpg** (0.31.0) - Async PostgreSQL driver
- **Alembic** (1.17.2) - Database migration tool
- **Pydantic** (2.12.5) - Data validation using Python type hints
- **Uvicorn** (0.38.0) - ASGI server

## 📁 Project Structure

```
crud/
├── src/
│   ├── __init__.py           # FastAPI app initialization
│   ├── config.py             # Configuration settings
│   ├── books/
│   │   ├── __init__.py
│   │   ├── routes.py         # Book API endpoints
│   │   ├── service.py        # Book business logic
│   │   └── schema.py         # Pydantic models for books
│   └── db/
│       ├── __init__.py
│       ├── main.py           # Database connection setup
│       └── models.py         # SQLModel database models
├── migrations/               # Alembic migration files
│   └── versions/
├── alembic.ini              # Alembic configuration
├── .env                     # Environment variables
├── .gitignore
└── README.md
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+**
- **PostgreSQL 12+**
- **pip** (Python package manager)
- **git** (optional, for version control)

## 🚀 Installation

### 1. Clone the repository (or navigate to your project directory)

```bash
cd /PYTHON/FASTAPI
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi==0.122.0 \
            sqlmodel==0.0.27 \
            asyncpg==0.31.0 \
            alembic==1.17.2 \
            pydantic==2.12.5 \
            pydantic-settings==2.12.0 \
            uvicorn==0.38.0
```

Or create a `requirements.txt` file with the above packages and run:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Create a `.env` file in the project root

```bash
touch .env
```

### 2. Add your database configuration

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
```

**Example:**
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/bookstore_db
```

> **Note:** Replace `username`, `password`, and `your_database_name` with your actual PostgreSQL credentials.

## 🗄️ Database Setup

### 1. Create a PostgreSQL database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE bookstore_db;

# Exit psql
\q
```

### 2. Run database migrations

```bash
# Apply all migrations
alembic upgrade head
```

This will create the following table structure:

**Books Table:**
- `uid` (UUID, Primary Key)
- `title` (String, 100 chars)
- `author` (String, 100 chars)
- `publisher` (String, 100 chars)
- `published_date` (DateTime)
- `page_count` (Integer)
- `language` (String, 50 chars)
- `created_at` (DateTime, auto-generated)
- `updated_at` (DateTime, auto-generated)

## ▶️ Running the Application

### Start the development server

```bash
uvicorn src:app --reload
```

The API will be available at: **http://127.0.0.1:8000**

### Access the interactive API documentation

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 📡 API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/v1/books
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/books/` | Get all books |
| `POST` | `/api/v1/books/` | Create a new book |
| `GET` | `/api/v1/books/{book_id}` | Get a book by ID (UUID) |
| `PATCH` | `/api/v1/books/{book_id}` | Update a book by ID |
| `DELETE` | `/api/v1/books/{book_id}` | Delete a book by ID |

### Example Requests

#### Create a Book (POST)

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Scribner",
    "published_date": "1925-04-10T00:00:00",
    "page_count": 180,
    "language": "English"
  }'
```

#### Get All Books (GET)

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/books/"
```

#### Get a Book by ID (GET)

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/books/{book_uuid}"
```

#### Update a Book (PATCH)

```bash
curl -X PATCH "http://127.0.0.1:8000/api/v1/books/{book_uuid}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "author": "Updated Author",
    "publisher": "Updated Publisher",
    "page_count": 200,
    "language": "English"
  }'
```

#### Delete a Book (DELETE)

```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/books/{book_uuid}"
```

## 🔄 Database Migrations

### Create a new migration

When you modify the database models in `src/db/models.py`, create a migration:

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migration

```bash
# Rollback one version
alembic downgrade -1

# Rollback to a specific version
alembic downgrade <revision_id>
```

### View migration history

```bash
alembic history
```

## 💻 Development

### Project Architecture

The project follows a layered architecture:

1. **Routes Layer** (`routes.py`) - API endpoints and request handling
2. **Service Layer** (`service.py`) - Business logic
3. **Schema Layer** (`schema.py`) - Pydantic models for validation
4. **Models Layer** (`models.py`) - Database models (SQLModel)

### Code Style

- Follow PEP 8 guidelines
- Use type hints throughout the code
- Keep functions focused and single-purpose
- Use async/await for database operations

### Running in Production

For production deployment, use a production-grade ASGI server:

```bash
uvicorn src:app --host 0.0.0.0 --port 8000 --workers 4
```

Or use gunicorn with uvicorn workers:

```bash
gunicorn src:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 🔐 Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Yes | `postgresql://user:pass@localhost:5432/db` |

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Happy Coding! 🚀**
