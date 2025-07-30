from pydantic_settings import BaseSettings

# settings.py
"""
Propósito: 

Centralizar configurações gerais do projeto, 
especialmente relacionadas a variáveis de ambiente, configuração de app, etc.

-> Define as variáveis de ambiente usando pydantic.BaseSettings ou dotenv.
-> Exemplo: URLs, chaves secretas, flags de debug, configurações gerais do app.
-> Pode conter lógicas para carregar .env automaticamente.    

"""

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
