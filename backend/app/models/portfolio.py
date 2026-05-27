from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"
    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"))
    name       = Column(String, default="My Portfolio")
    created_at = Column(DateTime, default=datetime.utcnow)
    owner      = relationship("User", back_populates="portfolios")
    holdings   = relationship("Holding", back_populates="portfolio")

class Holding(Base):
    __tablename__ = "holdings"
    id           = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    company_id   = Column(Integer, ForeignKey("companies.id"))
    shares       = Column(Float, nullable=False)
    buy_price    = Column(Float, nullable=False)
    buy_date     = Column(DateTime)
    portfolio    = relationship("Portfolio", back_populates="holdings")
