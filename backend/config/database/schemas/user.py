from pydantic import BaseModel, EmailStr
from config.database.models.user import User

# Registro de usuários
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

# GET de usuários
class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

    class Config:
        from_attributes = True

# Usado no Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str