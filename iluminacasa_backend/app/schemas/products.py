from pydantic import BaseModel
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


# Como é uma API externa, não é necessário validar os dados recebidos.
# Pois não há como alterar os dados que vêm do DummyJSON.

class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discount: Union[float, None] = None
    brand: str
    tags: List[str]
    images: List[str]