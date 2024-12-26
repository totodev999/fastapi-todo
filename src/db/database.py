from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

db_string = os.getenv("POSTGRES_STRING")


DATABASE_URL = db_string

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
