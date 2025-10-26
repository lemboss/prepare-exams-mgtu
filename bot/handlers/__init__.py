from aiogram import Router

from .commands import commands_router 
from .dialogs.menu.dialog import menu_dialog


def get_routers() -> list[Router]:
    return [
        commands_router,
        menu_dialog,
    ]