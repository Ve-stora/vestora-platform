from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.portfolio import Portfolio, Holding
from app.schemas.portfolio import HoldingCreate, PortfolioOut

router = APIRouter()

@router.get("/{user_id}", response_model=PortfolioOut)
def get_portfolio(user_id: int, db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == user_id).first()
    if not portfolio:
        portfolio = Portfolio(user_id=user_id)
        db.add(portfolio); db.commit(); db.refresh(portfolio)
    return portfolio

@router.post("/{user_id}/holdings")
def add_holding(user_id: int, payload: HoldingCreate, db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == user_id).first()
    holding = Holding(portfolio_id=portfolio.id, **payload.model_dump())
    db.add(holding); db.commit(); db.refresh(holding)
    return holding
