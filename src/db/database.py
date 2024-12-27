from fastapi import Depends
from typing import Annotated
from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

from classes.errors.DB import DBCommonException
from utils.custom_formatter import app_logger

load_dotenv()

db_string = os.getenv("POSTGRES_STRING")


DATABASE_URL = db_string

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    session = Session(engine)
    try:
        app_logger.info("db session created")
        yield session
    except Exception as e:
        app_logger.error(f"db error: {str(e)}")
        session.rollback()
        raise DBCommonException()
    finally:
        session.close()


sessionDep = Annotated[Session, Depends(get_session)]
