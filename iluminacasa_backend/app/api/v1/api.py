from fastapi import APIRouter
from api.v1.auth import router as auth_router
from api.v1.product import router as products_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(products_router)
