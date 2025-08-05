# config/database/database.py

from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from config.settings import settings

# Garantir que o .env seja carregado — normalmente feito em settings.py, mas se quiser segurança extra:
# from dotenv import load_dotenv
# load_dotenv()

"""
Propósito: Tudo que tem a ver com o banco de dados.

-> Criar a engine de conexão (SQLModel.create_engine).
-> Configurar sessão sync.
-> Inicializar conexão.
-> Funções utilitárias para acesso ao banco.

Estrutura recomendada:
config/database/models/*.py
    - Ex: users.py, products.py, orders.py
"""

# Caso queira usar SQLite por padrão em desenvolvimento:
# sqlite_url = "sqlite:///iluminacasa.db"
# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Adaptação automática para SQLite (caso esteja usando em desenvolvimento):
connect_args = {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}

# Criação da engine usando URL do settings
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

# Criação das tabelas com base nos modelos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Função de dependência que fornece a sessão do banco
def get_session():
    with Session(engine) as session:
        yield session

# Tipo dependente para uso em rotas
SessionDep = Annotated[Session, Depends(get_session)]
