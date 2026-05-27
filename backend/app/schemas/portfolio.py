from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PortfolioHoldingResponse(BaseModel):
    id: int
    stock_id: int
    quantity: float
    purchase_price: float
    current_value: float
    purchase_date: datetime
    
    class Config:
        from_attributes = True

class PortfolioBase(BaseModel):
    name: str
    description: Optional[str] = None

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioResponse(PortfolioBase):
    id: int
    user_id: int
    total_value: float
    total_invested: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class PortfolioDetailResponse(PortfolioResponse):
    holdings: List[PortfolioHoldingResponse] = []

class AddHoldingRequest(BaseModel):
    stock_id: int
    quantity: float
    purchase_price: float
    purchase_date: datetime