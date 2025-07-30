from typing import Annotated 
from sqlmodel import SQLModel, Field

"""
Tabela para representar um usuário.




"""

class UserBase(SQLModel):
    email: str
    first_name: str
    last_name: str

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class UserPublic(UserBase):
    id: int

class UserCreate(UserBase):
    password: str

class UserUpdate(SQLModel):
    email: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    first_name: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    last_name: Annotated[str, Field(min_length=5, max_length=100)] | None = None
    password: Annotated[str, Field(min_length=8, max_length=100)] | None = None