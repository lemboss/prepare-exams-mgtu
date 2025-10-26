from sqlalchemy.orm import Mapped

from ...database import Base, date_pk, created_at

class DailyProgress(Base):
    __tablename__ = 'daily_progress'

    date: Mapped[date_pk]
    hours: Mapped[float]
    created_at: Mapped[created_at]
    
    def __repr__(self) -> str:
        return f"DailyProgress: date={self.date}, hours={self.hours}"