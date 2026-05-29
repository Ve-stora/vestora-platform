from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PortfolioItemCreate(BaseModel):
    stock_id: int
    quantity: int
    purchase_price: float

class PortfolioResponse(BaseModel):
    id: int
    user_id: int
    total_value: float
    created_at: datetime

    class Config:
        from_attributes = True

class PortfolioCreate(BaseModel):
    user_id: int