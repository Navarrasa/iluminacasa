from fastapi import FastAPI
from api.v1.api import router as api_router
# Importar Tabelas
from config.database.models.user import User
from config.middleware.config import configure_middleware

from config.database.config import create_db_and_tables

class BaseConfig:
    title: str = "IluminaCasa API"
    description: str = "API para gerenciar produtos, usuários e pedidos na IluminaCasa."
    version: str = "1.0.0"

    def __init__(self):
        self.app = FastAPI(
            title=self.title,
            description=self.description,
            version=self.version,
        )

    def create_app(self):
        # Criar banco de dados
        create_db_and_tables()
        
        # Configurar middlewares
        configure_middleware(self.app)

        # Criar rotas
        self.app.include_router(api_router, prefix="/api/v1")
        return self.app


# Cria a instância da aplicação FastAPI
base_config = BaseConfig()
app = base_config.create_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}