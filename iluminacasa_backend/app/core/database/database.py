from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine, Field

"""

IluminaCasa Backend - Configuração do Banco de Dados

Este arquivo é o responsável por configurar a conexão com o banco de dados
Usando SQLModel e Pydantic para definir o modelo de dados.
Inclui a criação do engine, base declarativa e sessão do banco de dados.


"""

# Tabelas do Banco de Dados:
# - Users
# - Orders
# - Cart
# - Auth (Login e Registro)

class UserBase(SQLModel):
    email: str
    first_name: str
    last_name: str

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class UserPublic(UserBase):
    id: int

class UserCreate(UserBase):
    password: str

class UserUpdate(SQLModel):
    email: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    first_name: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    last_name: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    password: Annotated[str, Field(min_length=8, max_length=100)] | None = None



# Nomear o arquivo do Banco de Dados
sqlite_file_name = "database.db"

# URL de conexão com o banco de dados SQLite
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Configurações do banco de dados
connect_args = {"check_same_thread": False}

# Criando a engine* de conexão com o banco de dados

# *Engine é a interface principal para interagir com o banco de dados.

engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]