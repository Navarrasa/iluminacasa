from schemas.auth import LoginSchema, RegisterSchema
from config.database.database import get_session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from config.database.models.user import User
from services.auth.security import create_access_token, verify_password, pwd_context
from config.settings import settings

async def userLogin(login_data: LoginSchema, db=Depends(get_session)):
    """
    Função para autenticar um usuário e retornar um token JWT ou sessão.
    """
    # Lógica para autenticar o usuário e gerar o token
    user = db.query(User).filter(User.email == login_data.email).first()
    # Verifica se o usuário existe e se a senha está correta
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Cria o token de acesso através do ID do usuário
    access_token = create_access_token({"sub": user.id})

    # Define o cookie de sessão com o token JWT
    response = JSONResponse(content={"message": "Logged in successfully!"})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",
        secure=False,  # só em produção com HTTPS
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
    return response

async def userRegister(register_data: RegisterSchema, db=Depends(get_session)):
    """
    Função para registrar um novo usuário.
    """
    # Lógica para registrar o usuário
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

async def userLogout():

    # Lógica para logout
    """
    Passos para realizar o logout:
    1. Delete o Cookie.
    2. Remova informações da sessão do usuário.
    """

    response = JSONResponse(content={"message": "Logged out!"})
    response.delete_cookie("access_token")
    return response
