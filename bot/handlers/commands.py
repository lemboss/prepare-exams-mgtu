from datetime import datetime
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMemberUpdated, BotCommand
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED
from .dialogs.menu.states import MenuSG

commands_router = Router()

@commands_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    commands = [
        BotCommand(command="all", description="Отчет за весь период подготовки"),
        BotCommand(command="weekly", description="Отчет за текущую неделю"),
        BotCommand(command="monthly", description="Отчет за этот месяц"),
    ]
    await dialog_manager.middleware_data.get("bot").set_my_commands(commands)
    await message.answer("/all - Отчет за весь период подготовки\n/weekly - Отчет за текущую неделю\n/monthly - Отчет за этот месяц")
    
@commands_router.message(Command("all"))
async def all_time_report(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.all_time, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.SEND)
    
@commands_router.message(Command("weekly"))
async def weekly_report(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.weekly, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.SEND)
    
@commands_router.message(Command("monthly"))
async def monthly_report(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.monthly, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.SEND)
    

@commands_router.message(Command("test"))
async def monthly_report(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.daily_report, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.SEND)