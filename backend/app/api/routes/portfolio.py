from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.portfolio import Portfolio, PortfolioHolding
from app.models.stock import Stock
from app.schemas.portfolio import PortfolioCreate, PortfolioResponse, AddHoldingRequest, PortfolioDetailResponse

router = APIRouter()

def get_current_user_id(db: Session = Depends(get_db)) -> int:
    return 1

@router.post("/", response_model=PortfolioResponse)
def create_portfolio(portfolio: PortfolioCreate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    db_portfolio = Portfolio(**portfolio.dict(), user_id=user_id)
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

@router.get("/", response_model=List[PortfolioResponse])
def get_user_portfolios(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    portfolios = db.query(Portfolio).filter(Portfolio.user_id == user_id).all()
    return portfolios

@router.get("/{portfolio_id}", response_model=PortfolioDetailResponse)
def get_portfolio(portfolio_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio).filter(
        Portfolio.id == portfolio_id,
        Portfolio.user_id == user_id
    ).first()
    
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    holdings = db.query(PortfolioHolding).filter(PortfolioHolding.portfolio_id == portfolio_id).all()
    portfolio.holdings = holdings
    return portfolio

@router.post("/{portfolio_id}/holdings", response_model=PortfolioDetailResponse)
def add_holding(portfolio_id: int, holding: AddHoldingRequest, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio).filter(
        Portfolio.id == portfolio_id,
        Portfolio.user_id == user_id
    ).first()
    
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    stock = db.query(Stock).filter(Stock.id == holding.stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    db_holding = PortfolioHolding(
        portfolio_id=portfolio_id,
        stock_id=holding.stock_id,
        quantity=holding.quantity,
        purchase_price=holding.purchase_price,
        current_value=holding.quantity * stock.price,
        purchase_date=holding.purchase_date
    )
    
    db.add(db_holding)
    portfolio.total_invested += holding.quantity * holding.purchase_price
    portfolio.total_value += holding.quantity * stock.price
    
    db.commit()
    db.refresh(portfolio)
    
    holdings = db.query(PortfolioHolding).filter(PortfolioHolding.portfolio_id == portfolio_id).all()
    portfolio.holdings = holdings
    return portfolio

@router.delete("/{portfolio_id}/holdings/{holding_id}")
def remove_holding(portfolio_id: int, holding_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio).filter(
        Portfolio.id == portfolio_id,
        Portfolio.user_id == user_id
    ).first()
    
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    holding = db.query(PortfolioHolding).filter(
        PortfolioHolding.id == holding_id,
        PortfolioHolding.portfolio_id == portfolio_id
    ).first()
    
    if not holding:
        raise HTTPException(status_code=404, detail="Holding not found")
    
    portfolio.total_invested -= holding.quantity * holding.purchase_price
    portfolio.total_value -= holding.current_value
    
    db.delete(holding)
    db.commit()
    
    return {"message": "Holding removed"}