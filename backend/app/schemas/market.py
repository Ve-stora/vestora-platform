from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CompanyOut(BaseModel):
    id: int
    symbol: str
    name: str
    sector: Optional[str]
    market_cap: Optional[float]
    class Config: from_attributes = True

class StockPriceOut(BaseModel):
    id: int
    company_id: int
    open_price: float
    close_price: float
    high_price: float
    low_price: float
    volume: int
    recorded_at: datetime
    class Config: from_attributes = True
