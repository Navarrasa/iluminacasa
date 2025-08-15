from fastapi import Depends
from sqlmodel import select, Session
from config.database.config import get_session
from config.database.schemas.user import UserLogin, UserCreate
from config.utils.security import verify_password, pwd_context
from fastapi.responses import JSONResponse
from config.database.models.user import User
from services.dependencies import get_user

async def login(login_data: UserLogin, db: Session):
    """
    Função para autenticar um usuário e retornar um token JWT ou sessão.
    """

    user = get_user(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password):
        return False
    return user

async def register(register_data: UserCreate, db=Depends(get_session)):
    """
    Função para registrar um novo usuário.
    """
    
    existing_user = get_user(db, register_data.email)
    if existing_user:   
        return JSONResponse(status_code=400, content={"message": "User already exists"})
    hashed_password = pwd_context.hash(register_data.password)
    user = User(
        email=register_data.email,
        password=hashed_password,
        username=register_data.username,
    )  
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def logout():
    """
    Passos para realizar o logout:
    1. Delete o Cookie.
    2. Remova informações da sessão do usuário.
    """

    response = JSONResponse(content={"message": "Logged out!"})
    response.delete_cookie("access_token")
    return response