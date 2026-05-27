from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HoldingCreate(BaseModel):
    company_id: int
    shares: float
    buy_price: float
    buy_date: Optional[datetime]

class HoldingOut(BaseModel):
    id: int
    company_id: int
    shares: float
    buy_price: float
    buy_date: Optional[datetime]
    class Config: from_attributes = True

class PortfolioOut(BaseModel):
    id: int
    name: str
    holdings: list[HoldingOut] = []
    class Config: from_attributes = True
