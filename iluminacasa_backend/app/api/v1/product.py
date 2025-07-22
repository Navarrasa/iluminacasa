from api.v1.api import router
from services.dummyjson import get_products, get_product

# Retorna todos os produtos da API
@router.get("/products", summary="List all products")
async def get_all_products():
    return await get_products()

# Retorna um produto específico da API
@router.get("/products/{product_id}", summary="Get a product by ID")
async def get_product_by_id(product_id: int):
    return await get_product(product_id)