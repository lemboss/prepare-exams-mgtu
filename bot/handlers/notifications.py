from datetime import datetime
from aiogram_dialog import StartMode, ShowMode
from .dialogs.menu.states import MenuSG

async def notify_send_report(bg_manager):
    await bg_manager.start(state=MenuSG.daily_report, 
                                mode=StartMode.RESET_STACK, 
                                show_mode=ShowMode.DELETE_AND_SEND)
    
async def notify_morning(bg_manager):
    await bg_manager.start(state=MenuSG.weekly, 
                                mode=StartMode.RESET_STACK, 
                                show_mode=ShowMode.DELETE_AND_SEND)