from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from config.database.schemas.user import UserCreate
from config.database.config import get_session
from services.auth.auth import login, register, logout

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

# register
@router.post("/register", summary="User Registration", response_model=UserCreate)
async def userRegistration(register_data: UserCreate, db=SessionDep):
    return await register(register_data, db)

# login

# logout
@router.post("/logout", summary="User logout")
async def logoutUser():
    return await logout()
