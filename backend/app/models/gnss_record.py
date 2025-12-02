
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.db import Base
import datetime

class GNSSRecord(Base):
    __tablename__ = "gnss_records"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    fix_mode = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
