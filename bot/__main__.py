import asyncio

from aiogram import Bot, Dispatcher, session
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import chat
from aiogram_dialog import setup_dialogs

from .config import settings
from .handlers import get_routers
from .middlewares import get_middlewares
from .scheduler import start_scheduler

import logging

logger = logging.getLogger(__name__)

async def main():    
    bot = Bot(token=settings.tgbot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(*get_routers())
    get_middlewares(dp)
    bg_manager_factory = setup_dialogs(dp)
    
    start_scheduler(bg_manager_factory, bot, chat_id=443587978)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())