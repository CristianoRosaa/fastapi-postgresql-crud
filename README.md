##  FastAPI PostgreSQL CRUD API

Simple CRUD API developed for backend learning using FastAPI, PostgreSQL, SQLAlchemy and Pydantic.

---

## Features

- Create users
- List users
- Get user by ID
- Update users
- Delete users
- PostgreSQL integration
- ORM with SQLAlchemy
- Data validation using Pydantic
- Environment variables with env. 
- Automatic API documentation with Swagger

---

## Technologies

- Python 
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- psycopg2-binary
- Uvicorn
- python-dotenv
- Git/GitHub

---

## Project Structure
```bash

├── api.py 
├── database.py 
├── models.py 
├── schemas.py 
├── requirements.txt 
├── .gitignore 
└── .env
```
---

## Installation 

1. Clone the repository

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

---

2. Access the project folder.

cd YOUR_REPOSITORY

---

3. Create the virtual environment 

python -m venv venv

---

4. Activate the Virtual environment

Windows 

venv\Scripts\Activate

---

5. Install dependencies

pip install -r requirements.txt

---

6. Configure the environment variables

Create a file .env in the project root:

DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost/postgres

--- 

7. Run the server

uvicorn api:app --reload

--- 

## API documentation

After starting the server, access:

http://127.0.0.1:8000/docs

The Swagger interface will be generated automatically.

---

## Concepts in pratice

- API REST
- CRUD Operations
- FastAPI
- ORM with SQLAlchemy
- Integration with PostgreSQL
- Pydantic validation
- Dependency Injection
- Environment Variables
- Version control with Git/GitHub

---

## Author

Cristiano Rosa