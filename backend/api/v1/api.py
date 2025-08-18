from fastapi import APIRouter
from api.v1.users import router as user_routes
from api.v1.product import router as product_routes

router = APIRouter()

router.include_router(user_routes)
router.include_router(product_routes)