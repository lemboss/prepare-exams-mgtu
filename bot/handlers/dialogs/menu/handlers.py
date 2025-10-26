import asyncio
import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from ...dialogs.menu.states import MenuSG


from bot.api.load import send_daily, update_daily

logger = logging.getLogger(__name__)

def is_float(input: str) -> str:
    print(input)
    if "," in input:
        input = input.replace(",", ".")
    try:
        input = float(input)
    except ValueError:
        raise ValueError
    return input   
    

async def wrong_number(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, error: ValueError):
    await message.answer("Нужно целое или нецелое число отправить. Повтори ввод")
    
    
async def correct_number(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, value: float):
    session = dialog_manager.middleware_data.get("session")
    await send_daily(session, value)
    await dialog_manager.start(state=MenuSG.weekly, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.SEND)