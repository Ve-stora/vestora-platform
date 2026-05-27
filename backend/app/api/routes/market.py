from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockResponse, StockUpdate

router = APIRouter()

@router.get("/stocks", response_model=List[StockResponse])
def get_all_stocks(db: Session = Depends(get_db)):
    stocks = db.query(Stock).all()
    return stocks

@router.get("/stocks/{symbol}", response_model=StockResponse)
def get_stock_by_symbol(symbol: str, db: Session = Depends(get_db)):
    stock = db.query(Stock).filter(Stock.symbol == symbol.upper()).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.get("/stocks/id/{stock_id}", response_model=StockResponse)
def get_stock_by_id(stock_id: int, db: Session = Depends(get_db)):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.post("/stocks", response_model=StockResponse)
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    existing = db.query(Stock).filter(Stock.symbol == stock.symbol.upper()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Stock already exists")
    
    db_stock = Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

@router.put("/stocks/{stock_id}", response_model=StockResponse)
def update_stock(stock_id: int, stock_update: StockUpdate, db: Session = Depends(get_db)):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    update_data = stock_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stock, key, value)
    
    db.commit()
    db.refresh(stock)
    return stock

@router.get("/market-overview")
def get_market_overview(db: Session = Depends(get_db)):
    stocks = db.query(Stock).limit(10).all()
    return {"total_stocks": len(stocks), "stocks": stocks}