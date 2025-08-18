from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from config.database.models.product import ProductDB
from config.database.models.user import User
# from config.database.schemas.products import LandingProducts
from config.database.config import get_session
from services.products.products import getAll
from services.dependencies import get_current_user

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

"""

Product Router

contains all the routes for product for DB population

GET all products
GET product by tags
GET procuct by brand
GET product by title


"""

# Popular banco de dados do backend
@router.get("/data/products", summary="Populate DB", response_model=ProductDB)
async def populate_products(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
    ):
    result = await getAll(db)
    return {"inserted": len(result)}

# Produtos que serão renderizados na landing page
# @router.get("/products", summary="Get all products", response_model=LandingProducts)
# async def getLandingpageProducts():
#     await pass