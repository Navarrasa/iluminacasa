from fastapi import APIRouter
from services.products.dummyjson import get_products, get_product
from schemas.products import ProductSchema

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", summary="List all products", response_model=ProductSchema)
async def get_all_products():
    return await get_products()

@router.get("/{product_id}", summary="Get a product by ID", response_model=ProductSchema)
async def get_product_by_id(product_id: int):
    return await get_product(product_id)
