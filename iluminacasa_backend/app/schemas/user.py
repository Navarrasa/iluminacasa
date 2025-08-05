from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    """
    Schema completo para representar um usuário, usado principalmente para leitura interna
    ou administração. Inclui todos os campos, inclusive técnicos.

    Attributes:
        id (int): Identificador único do usuário.
        email (str): Email do usuário.
        password (str): Hash da senha (não deve ser retornada para clientes).
        first_name (str): Primeiro nome do usuário.
        last_name (str): Sobrenome do usuário.
        is_active (bool): Indica se o usuário está ativo.
        is_admin (bool): Indica se o usuário tem privilégios administrativos.
        created_at (datetime): Data de criação do usuário.
        updated_at (datetime): Última modificação (se houver).
    """
    id: int
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserPublicSchema(BaseModel):
    """
    Schema público para retorno de dados do usuário, ocultando campos sensíveis como senha.

    Usado em endpoints de resposta como `/me` ou `/users/{id}`.
    """
    id: int
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    """
    Schema de entrada para criação de novo usuário.

    Campos:
        email: Email do usuário.
        password: Senha em texto plano (será hashada).
        first_name: Primeiro nome.
        last_name: Último nome.
    """
    email: EmailStr = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=8, max_length=100)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)


class UserLoginSchema(BaseModel):
    """
    Schema de entrada para login de usuário.
    """
    email: EmailStr
    password: str


class UserUpdateSchema(BaseModel):
    """
    Schema de atualização parcial de usuário.
    Todos os campos são opcionais.
    """
    email: Optional[EmailStr] = Field(None, min_length=5, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)

    class Config:
        from_attributes = True
