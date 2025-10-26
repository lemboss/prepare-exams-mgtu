from aiogram import Router

from .access_middleware import AccessMiddleware 
from .di_session_middleware import SessionSqlalchemyMiddleware

def get_middlewares(dp):
    
    mw = [
        AccessMiddleware,
        SessionSqlalchemyMiddleware,
    ]
    
    for m in mw:
        dp.update.middleware(m())