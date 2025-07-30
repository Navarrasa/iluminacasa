from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from config.settings import settings
from models import *

# database.py
"""
Propósito: Tudo que tem a ver com o banco de dados.

-> Criar a engine de conexão (por ex, SQLModel.create_engine() ou SQLAlchemy engine).
-> Configurar sessão async/sync.
-> Inicializar conexão.
-> Funções utilitárias para acesso ao banco.

config/database/models/*.py

-> Arquivos com os modelos/tabelas SQLModel ou ORM.
-> Cada arquivo pode agrupar modelos por domínio, ex: users.py, products.py, orders.py.
-> Organizar modelos facilita manutenção e evita arquivos muito grandes.

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
