from datetime import date, datetime, timedelta
from .utils import MONTHS_RU
from ..config import settings
from ..database.repositories.daily_progress import DailyProgressRepository

async def by_all_time(session):
    # запросил данные за все время
    # рассчитал сколько всего готовился и сколько нужно
    # рассчитал %
    
    records = await DailyProgressRepository(session).get_all()
    prepared = sum(map(lambda v: v.hours, records))
    to_prepare_hours = (settings.settings.last_prepare_date - settings.settings.start_prepare_date).days // 7 * settings.settings.prepare_per_week
    prepared_percent = prepared / to_prepare_hours * 100 
    
    today = datetime.today()
    last_prepare_day = settings.settings.last_prepare_date
    days_remains = (last_prepare_day - today).days
    return {
        "prepare_time": to_prepare_hours,
        "prepared": int(prepared),
        "prepared_percent": int(prepared_percent),
        "days_remains": days_remains
    }

async def by_weekly(session, d: date):    
    # запросил данные за неделю по дате
    # рассчитал сколько на неделе готовился и сколько нужно не менее
    
    monday = d - timedelta(days=d.weekday())
    monday = monday.replace(hour=0, minute=0, second=0)
    sunday: datetime = monday + timedelta(days=6)
    sunday = sunday.replace(hour=23, minute=59)

    records = await DailyProgressRepository(session).get_by_period(monday, sunday)
    prepared = sum(map(lambda v: v.hours, records))
    
    prepare_time = settings.settings.prepare_per_week
    return {
        "prepare_time": prepare_time,
        "prepared": int(prepared),
    }
    
async def by_monthly(session, d: date):
    # запросил данные за месяц по дате
    # вернул месяц, сколько часов готовился по факту и по плану, рассчитал %
    
    first_day = d.replace(day=1)
    
    if d.month == 12:
        next_month = d.replace(year=d.year + 1, month=1, day=1)
    else:
        next_month = d.replace(month=d.month + 1, day=1)

    last_day = next_month - timedelta(days=1)
    
    records = await DailyProgressRepository(session).get_by_period(first_day, last_day)
    prepared = sum(map(lambda v: v.hours, records))
    
    prepare_per_month = settings.settings.prepare_per_week * 4
    prepared_percent = prepared / prepare_per_month * 100 
    return {
        "month": MONTHS_RU[first_day.month],
        "at_month": int(prepared),
        "hours_per_month": prepare_per_month,
        "hours_prepared_percent": int(prepared_percent)
    }
    