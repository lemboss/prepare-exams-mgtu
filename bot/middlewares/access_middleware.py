from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.config import settings

class AccessMiddleware(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data
    ) -> Any:
        user = data["event_from_user"]
        if settings.tgbot.admin == user.id: 
            return await handler(event, data)
        
        return await data["bot"].send_message(chat_id=user.id, text="Обратитесь к администратору")
 
        