from api.v1.api import router
from services.auth.auth_service import userLogin, userRegister, userLogout
from schemas.auth import LoginSchema, RegisterSchema

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

@router.post("/auth/login", summary="User login", response_model=LoginSchema)
async def loginUser(login: LoginSchema):
    return await userLogin(login)


@router.post("/auth/register", summary="User registration", response_model=RegisterSchema)
async def registerUser(register: RegisterSchema):
    return await userRegister(register)


@router.post("/auth/logout", summary="User logout")
async def logoutUser():
    return await userLogout()
