# About

This repo is an API server using following libraries.

- FastAPI
- SQLmodel
- Alembic

This repo could be my template for developing an API server using Python.

## Feature

1. Production-ready level logging
   This repo's logging feature is enough for production. This feature is built on FastAPI's middleware and logging module and contextvars.

2. DB Migration
   DB Migration is built on Alembic and SQLmodel.

3. Clean Architecture
   Under building.

### Detail

1. Production-ready level logging
   Access log, error log and Uvicorn log are logged in the same format. This makes it easier to handle logs.
   This is achieved by settings for standard logging library and contextvars for storing each requests info.

2. DB Migration
   Mainly thanks to Alembic, this is easily done. I just added small changes into env.py and script.py.mako.

3. Clean Architecture

## Preparation

1. Create virtual environment

```
python -m venv fastapi-todo-env
```

2. Activate virtual environment

```
source fastapi-todo-env/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create .env

```
POSTGRES_STRING="postgresql+psycopg2://username:password@localhost/your_db_name"
```

5. Migration

```
# Below command is not needed in this repo.
alembic init alembic

# Detect changes and create migration file.
alembic revision --autogenerate -m "your comment"

# Upgrade tables to the latest
alembic upgrade head

# Upgrade tables by 2 generations
alembic upgrade +2

# Upgrade tables to the specified revision_id
alembic upgrade revision_id
```

6. Run server

```
python main.py
```
