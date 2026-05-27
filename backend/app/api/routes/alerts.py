from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.alert import Alert

router = APIRouter()

@router.get("/{user_id}")
def get_alerts(user_id: int, db: Session = Depends(get_db)):
    return db.query(Alert).filter(Alert.user_id == user_id).all()

@router.post("/{user_id}")
def create_alert(user_id: int, company_id: int, alert_type: str,
                 threshold: float, db: Session = Depends(get_db)):
    alert = Alert(user_id=user_id, company_id=company_id,
                  alert_type=alert_type, threshold=threshold)
    db.add(alert); db.commit(); db.refresh(alert)
    return alert

@router.delete("/{alert_id}")
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if alert:
        db.delete(alert); db.commit()
    return {"message": "Alert deleted"}
