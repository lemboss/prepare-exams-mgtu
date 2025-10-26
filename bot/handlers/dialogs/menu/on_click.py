from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from .states import MenuSG

async def to_missed_leaders(_: CallbackQuery, __: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(MenuSG.menu, show_mode=ShowMode.EDIT)