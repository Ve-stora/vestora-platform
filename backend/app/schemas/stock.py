from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StockCreate(BaseModel):
    symbol: str
    name: str
    sector: Optional[str]
    price: float
    opening_price: Optional[float]
    high_price: Optional[float]
    low_price: Optional[float]
    volume: Optional[int]
    market_cap: Optional[float]
    pe_ratio: Optional[float]
    dividend_yield: Optional[float]

class StockResponse(BaseModel):
    id: int
    symbol: str
    name: str
    sector: Optional[str]
    price: float
    pe_ratio: Optional[float]
    dividend_yield: Optional[float]
    created_at: datetime

    class Config:
        from_attributes = True

class StockUpdate(BaseModel):
    price: Optional[float] = None
    opening_price: Optional[float] = None
    high_price: Optional[float] = None
    low_price: Optional[float] = None
    volume: Optional[int] = None