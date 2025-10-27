from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from .handlers.notifications import notify_send_report, notify_morning

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

def start_scheduler(bg_manager, bot, chat_id):
    manager = bg_manager.bg(
        chat_id=chat_id,
        user_id=chat_id,
        bot=bot
    )
    
    scheduler.add_job(
        notify_send_report, 
        CronTrigger(hour=19),
        kwargs={"bg_manager": manager})
    
    scheduler.add_job(
        notify_morning, 
        CronTrigger(hour=5),
        kwargs={"bg_manager": manager})
    
    scheduler.start()