from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from config.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(email: str, expires_delta: timedelta | None = None):
    to_encode = {"sub": email}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire}) # type: ignore
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def safe_hash_password(password: str) -> str:
    """
    Garante que a senha seja truncada corretamente em no máximo 72 bytes,
    sem cortar caracteres multibyte (como emojis ou acentos).
    """
    max_bytes = 72
    encoded = password.encode("utf-8")
    
    if len(encoded) <= max_bytes:
        return pwd_context.hash(password)
    
    # Trunca sem quebrar caracteres multibyte
    truncated = encoded[:max_bytes]
    while True:
        try:
            safe_password = truncated.decode("utf-8")
            break
        except UnicodeDecodeError:
            # Se o truncamento cortou um caractere, remove o último byte
            truncated = truncated[:-1]
    
    return pwd_context.hash(safe_password)
