from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import JSON

"""

Product database

contains all the columns about product information

"""

class ProductDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    price: float
    discount: float
    rating: float
    stock: int
    tags: list[str] = Field(sa_column=Column(JSON))
    brand: str
    warranty: str
    reviews: list[str] = Field(sa_column=Column(JSON))
    image: list[str] = Field(sa_column=Column(JSON))
