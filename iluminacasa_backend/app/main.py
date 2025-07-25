from fastapi import FastAPI
from api.v1 import product
from core.database.database import create_db_and_tables

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
        
        # Creating the database and tables
        create_db_and_tables()

        # Main Routers
        self.app.include_router(product.router, prefix="/products", tags=["products"])
        # self.app.include_router(auth.router, prefix="/auth", tags=["auth"])
        # self.app.include_router(cart.router, prefix="/cart", tags=["cart"])
        # self.app.include_router(orders.router, prefix="/orders", tags=["orders"])
        
        #   User Routers
        #  self.app.include_router(users.router, prefix="/users", tags=["users"])

        return self.app


# Create the FastAPI app instance
base_config = BaseConfig()
app = base_config.create_app()