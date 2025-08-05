import httpx

DUMMYJSON_URL = "https://dummyjson.com/products?limit=10"

async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(DUMMYJSON_URL)
        response.raise_for_status()
        data = response.json()
        return {"products": data["products"]}

async def get_product(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DUMMYJSON_URL}/{product_id}")
        response.raise_for_status()
        return response.json()