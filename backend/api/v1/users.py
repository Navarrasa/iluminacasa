from fastapi import APIRouter, Depends
from config.database.schemas.user import UserCreate
from config.database.config import SessionDep
from services.auth.auth import login, register, logout

router = APIRouter()

# register
@router.post("/register", summary="User Registration", response_model=UserCreate)
async def userRegistration(register_data: UserCreate, db=Depends(SessionDep)):
    return await register(register_data, db)

# login

# logout
@router.post("/logout", summary="User logout")
async def logoutUser():
    return await logout()