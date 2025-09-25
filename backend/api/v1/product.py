from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from config.database.models.product import ProductDB
from config.database.models.user import User
# from config.database.schemas.products import LandingProducts
from config.database.config import get_session
from services.products.products import getAll
from services.dependencies import get_current_user
from services.products.products import getBestSellers, getAllProducts
from config.database.schemas.products import LandingProducts, ProductReviews

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
    db: Session = Depends(get_session)
    ):
    result = await getAll(db)
    return {"inserted": len(result)}


# Best Sellers, produtos que serão renderixados na Landing Page
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

# GET /cart — mostrar itens no carrinho do usuário

# POST /cart — adicionar produto ao carrinho

# PUT /cart/:productId — alterar quantidade do produto no carrinho

# DELETE /cart/:productId — remover produto do carrinho

# DELETE /cart — esvaziar carrinho

# Pedidos (Orders)

# POST /orders — criar pedido (checkout)

# GET /orders/:id — detalhes do pedido

# GET /orders — listar pedidos do usuário

# PUT /orders/:id/cancel — cancelar pedido (se possível)

# GET /orders/status/:status — listar pedidos por status (pendente, enviado, entregue)

# Reviews e Avaliações

# POST /products/:id/reviews — criar review para um produto

# GET /products/:id/reviews — listar reviews do produto

# PUT /reviews/:id — editar review (somente dono)

# DELETE /reviews/:id — excluir review (somente dono)