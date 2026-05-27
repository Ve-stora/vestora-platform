from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StockBase(BaseModel):
    symbol: str
    name: str
    price: float

class StockCreate(StockBase):
    sector: Optional[str] = None
    opening_price: Optional[float] = None
    high_price: Optional[float] = None
    low_price: Optional[float] = None

class StockResponse(StockBase):
    id: int
    sector: Optional[str]
    opening_price: Optional[float]
    high_price: Optional[float]
    low_price: Optional[float]
    volume: Optional[int]
    market_cap: Optional[float]
    pe_ratio: Optional[float]
    dividend_yield: Optional[float]
    last_updated: datetime
    
    class Config:
        from_attributes = True

class StockUpdate(BaseModel):
    price: Optional[float] = None
    opening_price: Optional[float] = None
    high_price: Optional[float] = None
    low_price: Optional[float] = None
    volume: Optional[int] = None