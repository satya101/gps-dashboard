
import asyncio
import threading
from app.clients.gridtraq_client import GridTraqClient
from app.services.gnss_service import save_gnss_records
from app.core.config import settings

def start_scheduler():
    async def job():
        client = GridTraqClient()
        data = await client.fetch_last_locations()
        items = data.get("LineItems", [])
        save_gnss_records(items)

    async def loop():
        while True:
            await job()
            await asyncio.sleep(settings.CRON_INTERVAL_MINUTES * 60)

    t = threading.Thread(target=lambda: asyncio.run(loop()))
    t.start()
