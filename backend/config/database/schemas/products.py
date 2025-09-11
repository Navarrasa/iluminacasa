from pydantic import BaseModel
from typing import List

"""
Schema que irá definir o que a API irá puxar para o banco de dados

-> title : Título do produto
-> description : Descrição
-> category : Categoria
-> price : Preço
-> discount : Desconto 
-> rating : Avaliação geral
-> stock : Quantidade em estoque
-> tags : Categorias filtragem
-> brand : Marca
-> warranty : Garantia
-> reviews : Revview de clientes
-> images : Imagem

"""

class Review(BaseModel):
    rating: int
    date: str
    reviewerName: str
    reviewerEmail: str


class Product(BaseModel):
    title: str
    description: str
    category: str
    price: float
    discount: float
    rating: float
    stock: int
    tags: List[str]
    brand: str
    warranty: str
    reviews: List[Review]
    image: List[str]


# Schema para renderizar produtos na landing page
class LandingProducts(BaseModel):
    title: str
    category: str
    price: float
    discount: float
    rating: float
    image: List[str]


class ProductReviews(BaseModel):
    title: str
    rating: float
    reviews: Review