from fastapi import FastAPI
from api.v1 import product

app = FastAPI()

app.include_router(product.router, prefix="/api/v1", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Welcome to the IluminaCasa API!"}