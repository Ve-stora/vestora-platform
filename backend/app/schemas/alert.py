from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertCreate(BaseModel):
    user_id: int
    stock_id: int
    alert_type: str
    threshold_value: float

class AlertResponse(BaseModel):
    id: int
    user_id: int
    stock_id: int
    alert_type: str
    threshold_value: float
    created_at: datetime

    class Config:
        from_attributes = True