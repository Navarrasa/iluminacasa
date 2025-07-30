# config/settings.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Carrega variáveis do .env automaticamente
load_dotenv()

"""
Propósito:

Centralizar configurações gerais do projeto.

-> Usa pydantic.BaseSettings para tipagem e validação.
-> Lê variáveis do ambiente (.env, docker, etc).
-> Pode conter lógicas adicionais se necessário (por exemplo: ambiente de produção, dev, etc).
"""

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        # Arquivo de variáveis de ambiente
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instância única que será importada onde necessário
db_settings = Settings() # type: ignore
