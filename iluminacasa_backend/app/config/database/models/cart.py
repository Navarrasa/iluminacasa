from sqlmodel import SQLModel, Field

class Cart(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int
    product_id: int
    quantity: int