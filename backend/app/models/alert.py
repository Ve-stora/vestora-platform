from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"))
    company_id   = Column(Integer, ForeignKey("companies.id"))
    alert_type   = Column(String)   # PRICE_ABOVE, PRICE_BELOW, DIVIDEND
    threshold    = Column(Float)
    is_active    = Column(Boolean, default=True)
    triggered_at = Column(DateTime, nullable=True)
    created_at   = Column(DateTime, default=datetime.utcnow)
    user         = relationship("User", back_populates="alerts")
