from sqlmodel import SQLModel, Field
import datetime
from datetime import datetime  # noqa: F811

"""
Order model for representing customer orders in the database.
This model includes fields for user ID, product ID, quantity, total price,
order status, and timestamps for creation and updates.
"""


class Order(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int
    product_id: int
    quantity: int
    total_price: float
    status: str = Field(default="pending")  # e.g., pending, completed, cancelled
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())