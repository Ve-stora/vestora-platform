from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.alert import Alert
from app.schemas.alert import AlertCreate, AlertResponse, AlertUpdate

router = APIRouter()

def get_current_user_id(db: Session = Depends(get_db)) -> int:
    return 1

@router.post("/", response_model=AlertResponse)
def create_alert(alert: AlertCreate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    db_alert = Alert(**alert.dict(), user_id=user_id)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/", response_model=List[AlertResponse])
def get_user_alerts(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    alerts = db.query(Alert).filter(Alert.user_id == user_id).all()
    return alerts

@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(
        Alert.id == alert_id,
        Alert.user_id == user_id
    ).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.put("/{alert_id}", response_model=AlertResponse)
def update_alert(alert_id: int, alert_update: AlertUpdate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(
        Alert.id == alert_id,
        Alert.user_id == user_id
    ).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    update_data = alert_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(alert, key, value)
    
    db.commit()
    db.refresh(alert)
    return alert

@router.delete("/{alert_id}")
def delete_alert(alert_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(
        Alert.id == alert_id,
        Alert.user_id == user_id
    ).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    db.delete(alert)
    db.commit()
    return {"message": "Alert deleted"}