
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.models.gnss_record import GNSSRecord

router = APIRouter()

@router.get("/devices")
def list_devices():
    db = SessionLocal()
    devs = db.query(GNSSRecord.device_id).distinct().all()
    db.close()
    return [d[0] for d in devs]
