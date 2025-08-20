from datetime import timedelta
from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import Annotated
from sqlmodel import Session
from config.database.schemas.user import UserCreate, UserLogin
from config.database.schemas.tokens import Token
from config.database.config import get_session
from services.auth.auth import login, register, logout
from config.config import settings
from config.utils.security import create_access_token


SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

# register
@router.post("/register", summary="User Registration", response_model=UserCreate)
async def userRegistration(register_data: UserCreate, db: SessionDep):
    return await register(register_data, db)

# login usando cookies
@router.post("/login", summary="User login", response_model=Token)
async def loginUser(form_data: UserLogin, db: SessionDep, response: Response):
    user = await login(form_data, db )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        email=user.email, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        # secure=True,
        # path="/",
        samesite="lax",
        max_age=60*60*24*7  # 7 days
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# logout
@router.post("/logout", summary="User logout")
async def logoutUser():
    return await logout()
