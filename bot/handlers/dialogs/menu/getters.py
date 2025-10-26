import datetime
from aiogram_dialog import DialogManager
from bot.api.statistics import by_all_time, by_monthly, by_weekly
from bot.quotes import quotes

async def getter_all_time(dialog_manager: DialogManager, **_):
    session = dialog_manager.middleware_data.get("session")
    data = await by_all_time(session)
    
    data["prepared"] = round(data["prepared"], 1)
    data["prepared_percent"] = int(data["prepared_percent"])

    getter = {
        "all_hours":                data["prepare_time"],
        "hours_prepared":           int(data["prepared"]),
        "hours_prepared_percent":   int(data["prepared_percent"]),
        "days_remain":              data["days_remains"]
    }
    return getter

async def getter_weekly(dialog_manager: DialogManager, **_):
    session = dialog_manager.middleware_data.get("session")
    today = datetime.datetime.now()
    data = await by_weekly(session, today)
    quote = quotes.get_any()
    getter = {
        "at_week": data.get("prepared", 0),
        "hours_per_week": data.get("prepare_time", 0),
        "quote_text": quote.quote,
        "quote_author": quote.author
    }
    return getter

async def getter_monthly(dialog_manager: DialogManager, **_):
    session = dialog_manager.middleware_data.get("session")
    today = datetime.datetime.now()
    data = await by_monthly(session, today)

    getter = {
        "month": data.get("month", None),
        "at_month": data.get("at_month", None),
        "hours_per_month": data.get("hours_per_month", None),
        "hours_prepared_percent": data.get("hours_prepared_percent", None)
    }
    return getter