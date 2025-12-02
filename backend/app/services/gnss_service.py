
from app.models.gnss_record import GNSSRecord
from app.core.db import SessionLocal
import datetime

def save_gnss_records(records):
    db = SessionLocal()
    for rec in records:
        ts = rec.get("MessageDatePosition")
        try:
            timestamp = datetime.datetime.fromisoformat(ts)
        except:
            timestamp = datetime.datetime.utcnow()
        db_rec = GNSSRecord(
            device_id=rec.get('SerialNo'),
            fix_mode=int(rec.get("FixMode", 0)),
            latitude=rec.get("Latitude", 0),
            longitude=rec.get("Longitude", 0),
            timestamp=timestamp
        )
        db.add(db_rec)
    db.commit()
    db.close()
