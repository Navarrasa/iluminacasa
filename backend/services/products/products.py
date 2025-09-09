import httpx
from sqlmodel import Session
from sqlalchemy import func
from sqlmodel import select

from config.database.models.product import ProductDB

async def getAll(db: Session):
    url = "https://dummyjson.com/products?limit=100"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    products = data.get("products", [])

    inserted_products = []
    for p in products:
        product = ProductDB(
            id=p["id"],
            title=p.get("title", ""),
            description=p.get("description", ""),
            category=p.get("category", ""),
            price=p.get("price", 0),
            discount=p.get("discountPercentage", 0),
            rating=p.get("rating", 0),
            stock=p.get("stock", 0),
            tags=p.get("tags", []),
            brand=p.get("brand", ""),
            warranty=p.get("warrantyInformation", "No warranty"),
            reviews=[r.get("comment", "") for r in p.get("reviews", [])],
            image=p.get("images", []),
        )
        db.merge(product)  # evita duplicação, atualiza se existir
        inserted_products.append(product)

    db.commit()
    return inserted_products


async def getBestSellers(db: Session):
    # Flow:
    """
    Faz uma requisição ao banco de dados
    Pega 12 itens aleatoriamente e retorna como um objeto
    para ser utilizado no frontend
    
    """
    statement = select(ProductDB).order_by(func.random()).limit(12)
    return db.exec(statement).all()



    