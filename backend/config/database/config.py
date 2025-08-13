from fastapi import Depends
from typing import Annotated
from config.config import settings
from sqlmodel import create_engine, SQLModel, Session

sqlite_file_name = "iluminacasa.db"

connect_args = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]