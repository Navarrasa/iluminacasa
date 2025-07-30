from pydantic import BaseModel, field_validator, Field
from typing import Annotated

"""
Auth Schema for user authentication and registration.

Contains the necessary fields for user login and registration,
including email, password, and optional fields for user details.

LoginSchema:

Attributes:
    email (str): User's email address.
    password (str): User's password.

Example:
    {
        "email": "user1@example.com",
        "password": "securepassword123",
    }

RegisterSchema:
Attributes:
    email (str): User's email address.
    password (str): User's password.
    first_name (str): User's first name.
    last_name (str): User's last name.

Example:
    {
        "email": "username@ezample.com",
        "password": "securepassword123",
        "first_name": "John",
        "last_name": "Doe",
    }
"""

class LoginSchema(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def validate_email(cls, value: str) -> str:
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        return value
    

class RegisterSchema(BaseModel):
    email: Annotated[str, Field(min_length=5, max_length=100)]
    password: Annotated[str, Field(min_length=8, max_length=100)]
    first_name: Annotated[str, Field(min_length=5, max_length=100)]
    last_name: Annotated[str, Field(min_length=5, max_length=100)]

    @field_validator("email")
    def validate_email(cls, value: str) -> str:
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        return value
    
    @field_validator("first_name", "last_name")
    def validate_name(cls, value: str) -> str:
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return value