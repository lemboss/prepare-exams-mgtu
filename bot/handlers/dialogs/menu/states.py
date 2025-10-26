from aiogram.fsm.state import State, StatesGroup

class MenuSG(StatesGroup):
    all_time = State()
    weekly = State()
    monthly = State() 
    daily_report = State()
    