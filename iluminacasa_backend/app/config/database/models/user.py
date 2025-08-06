from typing import Annotated
from datetime import datetime
from pydantic import EmailStr, BaseModel
from sqlmodel import SQLModel, Field

# SQLModel
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None


# Schemas Pydantic (table=False por padrão)
class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str  # texto plano, será hashado antes de salvar


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str


class UserInDB(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool
    is_admin: bool


# UserCreate → usado para receber dados do usuário e hash da senha.

# UserInDB → usado internamente, contém hash e flags.

# UserPublic → enviado para o cliente, sem senha.