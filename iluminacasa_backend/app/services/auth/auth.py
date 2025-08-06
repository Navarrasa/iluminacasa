from sqlmodel import select
from schemas.auth import LoginSchema, RegisterSchema
from config.database.database import get_session
from fastapi import Depends
from fastapi.responses import JSONResponse
from config.database.models.user import User
from services.auth.security import verify_password, pwd_context
from services.dependencies import get_user
from sqlmodel import Session

async def login(login_data: LoginSchema, db: Session):
    """
    Função para autenticar um usuário e retornar um token JWT ou sessão.
    """
    # Lógica para autenticar o usuário e gerar o token
    user = get_user(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password):
        return False
    return user

async def register(register_data: RegisterSchema, db=Depends(get_session)):
    """
    Função para registrar um novo usuário.
    """
    # Lógica para registrar o usuário
    existing_user = db.exec(select(User).where(User.email == register_data.email)).first()
    if existing_user:   
        return JSONResponse(status_code=400, content={"message": "User already exists"})
    hashed_password = pwd_context.hash(register_data.password)
    user = User(
        email=register_data.email,
        password=hashed_password,
        first_name=register_data.first_name,
        last_name=register_data.last_name,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def logout():

    # Lógica para logout
    """
    Passos para realizar o logout:
    1. Delete o Cookie.
    2. Remova informações da sessão do usuário.
    """

    response = JSONResponse(content={"message": "Logged out!"})
    response.delete_cookie("access_token")
    return response
