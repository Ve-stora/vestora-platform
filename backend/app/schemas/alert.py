from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertBase(BaseModel):
    stock_id: int
    alert_type: str
    target_value: Optional[float] = None
    message: Optional[str] = None

class AlertCreate(AlertBase):
    pass

class AlertResponse(AlertBase):
    id: int
    user_id: int
    is_active: bool
    created_at: datetime
    triggered_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class AlertUpdate(BaseModel):
    target_value: Optional[float] = None
    is_active: Optional[bool] = None