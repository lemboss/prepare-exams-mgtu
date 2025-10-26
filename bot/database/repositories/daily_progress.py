from ..models.daily_progress import DailyProgress

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime

class DailyProgressRepository():
    def __init__(self, session: AsyncSession, model = DailyProgress):
        self.session = session
        self.model = model
        
    async def get_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return res.scalars().all()
    
    async def get_by_period(self, date_from, date_to):
        stmt = select(self.model).filter(self.model.date > date_from, self.model.date < date_to)
        res = await self.session.execute(stmt)
        return res.scalars().all()
        
    async def add(self, hours):
        date = datetime.now().date()
        self.session.add(self.model(date = date, hours=hours))
        
    async def update(self, date: datetime, hours: float):
        query = (
            update(self.model)
            .filter(self.model.date == date)
            .values(hours=hours)
        )
        await self.session.execute(query)