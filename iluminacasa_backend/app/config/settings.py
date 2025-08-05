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
    # Banco de dados
    DATABASE_URL: str

    # JWT / Segurança
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instância única para uso global
settings = Settings()  # type: ignore
