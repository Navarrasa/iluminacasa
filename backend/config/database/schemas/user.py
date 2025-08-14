from pydantic import BaseModel, EmailStr

# Registro de usuários
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

# GET de usuários
class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True

# Usado no Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
