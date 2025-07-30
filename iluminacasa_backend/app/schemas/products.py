from pydantic import BaseModel
from typing import List, Optional

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

class Dimensions(BaseModel):
    width: float
    height: float
    depth: float

class Review(BaseModel):
    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str

class Meta(BaseModel):
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str

class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: Optional[float] = None
    rating: Optional[float] = None
    stock: Optional[int] = None
    tags: List[str]
    brand: str
    sku: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[Dimensions] = None
    warrantyInformation: Optional[str] = None
    shippingInformation: Optional[str] = None
    availabilityStatus: Optional[str] = None
    reviews: Optional[List[Review]] = None
    returnPolicy: Optional[str] = None
    minimumOrderQuantity: Optional[int] = None
    meta: Optional[Meta] = None
    images: List[str]
    thumbnail: Optional[str] = None

class ProductListResponse(BaseModel):
    products: List[ProductSchema]
