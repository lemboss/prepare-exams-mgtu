from datetime import datetime
from bot.database.repositories.daily_progress import DailyProgressRepository


async def send_daily(session, hours=0):
    await DailyProgressRepository(session).add(hours)
    await session.commit()
    
async def update_daily(session, date: datetime, hours: float):
    await DailyProgressRepository(session).update(date, hours)
    await session.commit()