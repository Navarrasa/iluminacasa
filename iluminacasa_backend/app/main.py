from fastapi import FastAPI
from api.v1 import product
# , auth, cart, orders, users

app = FastAPI()

app.include_router(product.router, prefix="/api/v1", tags=["products"])
# app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
# app.include_router(cart.router, prefix="/api/v1", tags=["cart"])
# app.include_router(orders.router, prefix="/api/v1", tags=["orders"])
# app.include_router(users.router, prefix="/api/v1", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the IluminaCasa API!"}
