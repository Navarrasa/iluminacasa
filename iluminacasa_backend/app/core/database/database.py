from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from core.config import settings

"""

IluminaCasa Backend - Configuração do Banco de Dados

Este arquivo é o responsável por configurar a conexão com o banco de dados
Usando SQLModel e Pydantic para definir o modelo de dados.
Inclui a criação do engine, base declarativa e sessão do banco de dados.

# Tabelas do Banco de Dados:
# - Users
# - Orders
# - Cart
# - Auth (Login e Registro)

"""

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# engine = create_engine(settings.DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
