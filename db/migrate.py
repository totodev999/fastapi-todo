from sqlmodel import SQLModel
from database import engine
import models


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    print("Creating database tables...")
    create_db_and_tables()
    print("Database tables created!")
