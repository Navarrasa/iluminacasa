from fastapi import APIRouter, Depends
from services.dependencies import get_current_active_user
from config.database.models.user import User
from schemas.user import UserPublicSchema

router = APIRouter(prefix="/user", tags=["user-info"])

@router.get("/me", summary="Get user information", response_model=UserPublicSchema)
async def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# @router.put("/me", response_model=UserPublicSchema)
# async def update_me(update_data: UserUpdateSchema, current_user: User = Depends(get_current_user)):
#     pass
