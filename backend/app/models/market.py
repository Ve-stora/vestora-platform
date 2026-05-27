from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base

class Company(Base):
    __tablename__ = "companies"
    id            = Column(Integer, primary_key=True, index=True)
    symbol        = Column(String, unique=True, index=True)
    name          = Column(String, nullable=False)
    sector        = Column(String)
    description   = Column(String)
    market_cap    = Column(Float)
    listed_date   = Column(DateTime)

class StockPrice(Base):
    __tablename__ = "stock_prices"
    id            = Column(Integer, primary_key=True, index=True)
    company_id    = Column(Integer, ForeignKey("companies.id"))
    open_price    = Column(Float)
    close_price   = Column(Float)
    high_price    = Column(Float)
    low_price     = Column(Float)
    volume        = Column(Integer)
    recorded_at   = Column(DateTime, default=datetime.utcnow)

class Dividend(Base):
    __tablename__ = "dividends"
    id            = Column(Integer, primary_key=True, index=True)
    company_id    = Column(Integer, ForeignKey("companies.id"))
    amount        = Column(Float)
    currency      = Column(String, default="UGX")
    record_date   = Column(DateTime)
    payment_date  = Column(DateTime)
    announced_at  = Column(DateTime, default=datetime.utcnow)
