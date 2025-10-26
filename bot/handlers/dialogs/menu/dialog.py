from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import TextInput

from bot.handlers.dialogs.menu.handlers import is_float, wrong_number, correct_number

from .getters import getter_all_time, getter_monthly, getter_weekly

from .states import MenuSG

menu_dialog = Dialog(
    Window(
        Format("Готовился <b>{hours_prepared}/{all_hours}</b> часов или <b>{hours_prepared_percent}/100%</b> от плана"),
        Format("До конца подготовки осталось <b>{days_remain}</b> дней"),
        state=MenuSG.all_time,
        getter=getter_all_time
    ),
    
    Window(
        Format("На этой неделе <b>{at_week}/{hours_per_week}</b> часов"),
        Format("<blockquote>{quote_text}\n<i>{quote_author}</i></blockquote>"),
        state=MenuSG.weekly,
        getter=getter_weekly
    ),    
    
    Window(
        Format("В {month} готовился <b>{at_month}/{hours_per_month}</b> часов или <b>{hours_prepared_percent}/100%</b> от месячного плана"),
        state=MenuSG.monthly,
        getter=getter_monthly
    ),   
    
    Window(
        Format("Сколько готовился сегодня?"),
        TextInput(
            id="daily_report",
            on_error=wrong_number,
            on_success=correct_number,
            type_factory=is_float,
        ),
        state=MenuSG.daily_report,
    ),        
)