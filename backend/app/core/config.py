
from pydantic import BaseSettings

class Settings(BaseSettings):
    GRIDTRAQ_DEVICE_IDENTIFIER: str
    GRIDTRAQ_USERNAME: str
    GRIDTRAQ_PASSWORD: str
    GRIDTRAQ_API_KEY: str
    DATABASE_URL: str
    CRON_INTERVAL_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
