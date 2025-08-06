from fastapi import APIRouter, Depends, HTTPException, status
from services.auth.auth import login, register, logout
from services.auth.security import create_access_token
from schemas.auth import LoginSchema, RegisterSchema
from config.database.database import get_session
from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from config.settings import settings
from config.database.models.token import Token
from sqlmodel import Session

"""
auth.py

Este módulo define as rotas e funcionalidades de autenticação para a API do website,
utilizando o framework FastAPI. Ele oferece suporte às operações de login, registro
(sign-up) e logout (sign-out) de usuários.

Funcionalidades incluídas:
- Login: autentica usuários existentes e retorna tokens JWT ou sessões.
- Sign-up: registra novos usuários, aplicando validações e persistindo dados no banco.
- Sign-out: encerra a sessão do usuário ou invalida o token.

Dependências típicas:
- FastAPI
- Pydantic
- HTTPBearer / OAuth2PasswordBearer (dependendo do método de autenticação usado)
- Database (e.g. SQLAlchemy, asyncpg)
- JWT (e.g. PyJWT ou jose)

Este módulo deve ser incluído no roteamento principal da aplicação para permitir
o gerenciamento seguro de sessões de usuário.

"""

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", summary="User login", response_model=Token)
async def loginUser(form_data: LoginSchema, db: Session = Depends(get_session) ) -> Token:
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
    return Token(access_token=access_token, token_type="bearer")

@router.post("/register", summary="User registration", response_model=RegisterSchema)
async def registerUser(register_data: RegisterSchema, db=Depends(get_session)):
    return await register(register_data, db)

@router.post("/logout", summary="User logout")
async def logoutUser():
    return await logout()
