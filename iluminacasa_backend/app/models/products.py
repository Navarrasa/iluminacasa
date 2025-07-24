from pydantic import BaseModel, field_validator
from typing import List, Union

"""
Schema para representar um produto.

Representa os dados essenciais de um produto para exibição e manipulação
na API IluminaCasa.

Attributes:
    id (int): Identificador único do produto.
    title (str): Nome do produto.
    description (str): Descrição detalhada do produto.
    category (str): Categoria do produto.
    price (float): Preço do produto em reais.
    discount (Optional[float]): Desconto aplicado ao produto (valor entre 0 e 1).
    brand (str): Marca do produto.
    tags (List[str]): Lista de tags associadas ao produto.
    image (List[str]): Lista de imagens associadas ao produto.

Example:
    {
        "id": 1,
        "title": "Luminária LED",
        "description": "Luminária de mesa com LED ajustável",
        "category": "iluminação",
        "price": 199.90,
        "discount": 0.15,
        "brand": "Lumina",
        "tags": ["LED", "mesa", "iluminação"],
        "images": ["https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp"],
    }
"""

class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discount: Union[float | 0]
    brand: str
    tags: List[str]
    images: List[str]

    # Validar que o campo preço não pode ser negativo
    @field_validator('price')
    def price_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('price must be zero or positive')
        return v
    
    # Validar que o campo desconto não pode ser negativo
    @field_validator('discount')
    def discount_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('discount must be zero or positive')
        return v
    