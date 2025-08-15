from sqlmodel import Session, select
from config.database.models.user import User
from jwt.exceptions import InvalidTokenError
import jwt
from fastapi import Depends, HTTPException, status, Request
from config.config import settings
from config.database.config import get_session


def get_user(db: Session, email: str):
    statement = select(User).where(User.email == email) # SELECT * FROM USUARIOS WHERE usuario.EMAIL == EMAIL
    result = db.exec(statement) # RESULTADO = EXECUÇÃO DO STATEMENT
    user = result.first() # USER = PRIMEIRO RESULTADO DA CONSULTA
    return user

def get_current_user(request: Request, db=Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = request.cookies.get("access_token")  # <- Busca o token do cookie

    if not token:
        raise credentials_exception

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = get_user(db, email)
    if user is None:
        raise credentials_exception

    return user