from fastapi import APIRouter
from app.services.market_service import get_market_overview, get_stock_data

router = APIRouter()

@router.get("/overview")
def market_overview():
    return get_market_overview()

@router.get("/stock/{symbol}")
def stock_detail(symbol: str):
    stock = get_stock_data(symbol)
    return stock or {"error": "Stock not found"}
