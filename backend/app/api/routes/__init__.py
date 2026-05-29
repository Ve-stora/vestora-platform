from fastapi import APIRouter
from app.api.routes import auth, market, portfolio, ai_assistant, alerts, education

router = APIRouter(prefix="/api")
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(market.router, prefix="/market", tags=["market"])
router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
router.include_router(ai_assistant.router, prefix="/ai", tags=["ai"])
router.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
router.include_router(education.router, prefix="/education", tags=["education"])