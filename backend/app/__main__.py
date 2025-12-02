
from fastapi import FastAPI
from app.api.routes import gnss, devices
from app.core.scheduler import start_scheduler

app = FastAPI()
app.include_router(gnss.router)
app.include_router(devices.router)
start_scheduler()
