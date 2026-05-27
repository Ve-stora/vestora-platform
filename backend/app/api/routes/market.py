from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.market import Company, StockPrice
from app.schemas.market import CompanyOut, StockPriceOut
from typing import List

router = APIRouter()

@router.get("/companies", response_model=List[CompanyOut])
def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()

@router.get("/companies/{symbol}", response_model=CompanyOut)
def get_company(symbol: str, db: Session = Depends(get_db)):
    return db.query(Company).filter(Company.symbol == symbol.upper()).first()

@router.get("/prices/{company_id}", response_model=List[StockPriceOut])
def get_prices(company_id: int, limit: int = 30, db: Session = Depends(get_db)):
    return db.query(StockPrice).filter(StockPrice.company_id == company_id)\
             .order_by(StockPrice.recorded_at.desc()).limit(limit).all()
