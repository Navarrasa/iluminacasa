from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from config.database.models.product import ProductDB
from config.database.models.user import User
# from config.database.schemas.products import LandingProducts
from config.database.config import get_session
from services.products.products import getAll
from services.dependencies import get_current_user
from services.products.products import getBestSellers, getAllProducts, searchProducts
from config.database.schemas.products import LandingProducts, ProductReviews

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

# Popular banco de dados do backend
@router.get("/data/products", summary="Populate DB", response_model=ProductDB)
async def populate_products(
    db: Session = Depends(get_session)
    ):
    result = await getAll(db)
    return {"inserted": len(result)}


# LANDING PAGE #

# Best Sellers, produtos que serão renderizados na Landing Page
@router.get("/products/best-sellers", summary="Best Sellers", response_model=list[LandingProducts])
async def best_sellers(
    db: Session = Depends(get_session),
    ):
    """
    Pega 12 itens aleatoriamente e retorna como um objeto
    para ser utilizado no frontend
    """
    result = await getBestSellers(db)
    return result

# Search bar na Landing page
@router.get("/search/", summary="Search Products", response_model=list[LandingProducts])
async def search_products(
    query: str,
    db: Session = Depends(get_session),
    ):
    """
    Realiza uma busca de produtos com base na query fornecida
    """
    result = await searchProducts(query, db)
    return result




@router.get("/products/reviews", summary="Get product reviews", response_model=list[ProductReviews])
async def product_reviews(
    db: Session = Depends(get_session),
    ):
    """
    Pega todas as avaliações de produtos e retorna como um objeto
    para ser utilizado no frontend
    """
    result = await getAllProducts(db)
    return result


# GET /products — listar produtos com filtros (categoria, preço, busca, etc)

# GET /products/:id — detalhes de um produto específico

# GET /products/best-sellers — produtos mais vendidos (como você já fez)

# GET /products/reviews — reviews aleatórios ou recentes (você também mencionou)

# GET /products/categories — listar categorias disponíveis (iluminação LED, halógena, etc)




# Reviews e Avaliações

# POST /products/:id/reviews — criar review para um produto

# GET /products/:id/reviews — listar reviews do produto

