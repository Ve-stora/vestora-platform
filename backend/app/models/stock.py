from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Stock(Base):
    __tablename__ = "stocks"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    sector = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    opening_price = Column(Float, nullable=True)
    high_price = Column(Float, nullable=True)
    low_price = Column(Float, nullable=True)
    volume = Column(Integer, nullable=True)
    market_cap = Column(Float, nullable=True)
    pe_ratio = Column(Float, nullable=True)
    dividend_yield = Column(Float, nullable=True)
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())