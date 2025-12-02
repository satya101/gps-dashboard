
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.models.gnss_record import GNSSRecord
import datetime

router = APIRouter()

@router.get("/devices/{device_id}/gnss/health")
def gnss_health(device_id: str):
    db = SessionLocal()
    week_ago = datetime.datetime.utcnow() - datetime.timedelta(days=7)
    recs = db.query(GNSSRecord).filter(
        GNSSRecord.device_id == device_id,
        GNSSRecord.timestamp >= week_ago
    ).all()
    db.close()

    if not recs:
        return {"device_id": device_id, "message": "No data"}

    total = len(recs)
    bad = len([r for r in recs if r.fix_mode < 3])
    bad_ratio = bad / total

    return {
        "device_id": device_id,
        "total": total,
        "bad_ratio": bad_ratio,
        "is_unhealthy": bad_ratio > 0.05
    }
