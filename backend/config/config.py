# config/settings.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Carrega variáveis do .env automaticamente
load_dotenv()

# Criando e setando as variáveis de ambiente .env

class Settings(BaseSettings):
    
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instância única para uso global
settings = Settings() # type: ignore