from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr | None = Field(unique=True, index=True)
    hashed_password: str
    is_admin: bool | None = Field(index=True, default=False)
    is_active: bool | None = Field(index=True, default=False)
    username: str | None = Field(index=True, max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)