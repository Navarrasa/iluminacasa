from pydantic import BaseModel, Field
from typing import Annotated

class UserSchema(BaseModel):
    """
    Schema para representar um Usuário.

    Representa os dados essenciais de um usuário para exibição e manipulação
    na API IluminaCasa.

    Attributes:
        id (int): Identificador único do usuário.
        email (str): Identificador do email do cliente.
        password (str): Senha criptografada do cliente.
        first_name(str): Primeiro nome do cliente.
        last_name(str): Último nome do cliente.

    Example:
        {
            "id": 1,
            "email": "example@gmail.com",
            "password": "example123",
            "first_name": "John",
            "last_name": "Doe",
        }
    """

    email: Annotated[str, Field(min_length=5, max_length=100)]
    password: Annotated[str, Field(min_length=8, max_length=100)]
    first_name: Annotated[str, Field(min_length=5, max_length=100)]
    last_name: Annotated[str, Field(min_length=5, max_length=100)]
