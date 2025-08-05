from typing import Annotated
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    """
    Esquema base para um usuário contendo os campos principais
    que serão compartilhados entre outras classes.

    Campos:
    - email: Email do usuário (validado como email válido).
    - first_name: Primeiro nome do usuário.
    - last_name: Sobrenome do usuário.
    """
    email: EmailStr
    first_name: Annotated[str, Field(min_length=2, max_length=50)]
    last_name: Annotated[str, Field(min_length=2, max_length=50)]


class User(UserBase, table=True):
    """
    Modelo que representa o usuário no banco de dados.

    Extende UserBase e adiciona:
    - id: Identificador único (chave primária).
    - password: Hash da senha do usuário (nunca armazenar senha em texto plano).
    - is_active: Indica se o usuário está ativo (pode ser usado para bloquear acesso).
    - is_admin: Flag para diferenciar usuários administradores.
    - created_at: Timestamp da criação do registro.
    - updated_at: Timestamp da última atualização (pode ser None).
    """
    id: int | None = Field(default=None, primary_key=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None


class UserPublic(UserBase):
    """
    Esquema para representar um usuário de forma pública,
    ou seja, para enviar dados para o cliente sem expor informações sensíveis.

    Inclui:
    - id: Identificador do usuário.
    (Não inclui senha nem flags administrativas)
    """
    id: int


class UserCreate(UserBase):
    """
    Esquema para criar um novo usuário.

    Inclui todos os campos necessários para cadastro:
    - email, first_name, last_name (do UserBase).
    - password: Senha em texto plano (será hashada antes de salvar).
    """
    password: Annotated[str, Field(min_length=8, max_length=100)]


class UserUpdate(SQLModel):
    """
    Esquema para atualização parcial dos dados do usuário.

    Todos os campos são opcionais (podem atualizar um ou mais campos):
    - email, first_name, last_name, password.
    (Usar validações mínimas para garantir integridade)
    """
    email: Annotated[EmailStr, Field(min_length=5, max_length=100)] | None = None
    first_name: Annotated[str, Field(min_length=2, max_length=50)] | None = None
    last_name: Annotated[str, Field(min_length=2, max_length=50)] | None = None
    password: Annotated[str, Field(min_length=8, max_length=100)] | None = None
