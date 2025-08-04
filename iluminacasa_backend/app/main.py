from fastapi import FastAPI
from api.v1.api import router as api_router
from config.database.database import create_db_and_tables

from config.database.models.orders import Order  # noqa: F401
from config.database.models.cart import Cart # noqa: F401
from config.database.models.user import User # noqa: F401

class BaseConfig:
    title: str = "IluminaCasa API"
    description: str = "API para gerenciar produtos, usuários e pedidos na IluminaCasa."
    version: str = "1.0.0"

    def __init__(self) -> None:
        self.app = FastAPI(
            title=self.title,
            description=self.description,
            version=self.version,
        )

    def create_app(self):
        # Configurações do banco de dados
        create_db_and_tables()

        # Main Router
        self.app.include_router(api_router, prefix="/api/v1")

        return self.app

# Cria a instância da aplicação FastAPI
base_config = BaseConfig()
app = base_config.create_app()
