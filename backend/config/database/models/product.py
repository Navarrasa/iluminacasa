from sqlmodel import SQLModel, Field, Column, JSON
from typing import List, Optional
from datetime import datetime

class ProductDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str
    name: str
    slug: Optional[str] = None
    brief_description: Optional[str] = None
    detailed_description: Optional[str] = None
    main_category: Optional[str] = None
    subcategories: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    
    price: float
    promotional_price: Optional[float] = None
    currency: Optional[str] = "BRL"
    
    current_stock: Optional[int] = None
    minimum_stock: Optional[int] = None
    situation: Optional[str] = None  # ativo/inativo
    
    weight: Optional[float] = None  # em gramas
    dimensions: Optional[dict] = Field(default=None, sa_column=Column(JSON))  # height, width, depth
    
    # Especificações técnicas
    tension: Optional[str] = None
    power: Optional[int] = None
    luminous_flow: Optional[int] = None
    color_temperature: Optional[str] = None
    color_reproduction_index: Optional[int] = None
    lamp_type: Optional[str] = None
    lamp_base: Optional[str] = None
    product_color: Optional[str] = None
    material: Optional[str] = None
    lifetime: Optional[int] = None
    protection_grade: Optional[str] = None
    
    # Outras informações
    images: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    manufacturer: Optional[str] = None
    brand: Optional[str] = None
    origin: Optional[str] = None
    warranty: Optional[int] = None  # em meses
    
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    
    registry_date: Optional[datetime] = None
