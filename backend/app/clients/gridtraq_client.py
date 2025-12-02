
import httpx
from app.core.config import settings

class GridTraqClient:
    BASE_URL = "https://devapi.gridtraqcentral.com"

    def __init__(self):
        self.token = None

    async def authenticate(self):
        url = f"{self.BASE_URL}/Users/Users_ValidateQ"
        params = {
            "deviceidentifier": settings.GRIDTRAQ_DEVICE_IDENTIFIER,
            "username": settings.GRIDTRAQ_USERNAME,
            "password": settings.GRIDTRAQ_PASSWORD,
            "Token-API": settings.GRIDTRAQ_API_KEY
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(url, params=params)
            data = r.json()
            self.token = data.get("UserToken")
            return self.token

    async def fetch_last_locations(self):
        if not self.token:
            await self.authenticate()
        url = f"{self.BASE_URL}/Vehicles/Vehicles_LastLocation"
        async with httpx.AsyncClient() as client:
            r = await client.post(url, json={"UserToken": self.token})
            return r.json()
