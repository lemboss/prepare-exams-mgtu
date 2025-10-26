from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.pool import NullPool
from sqlalchemy import text, BIGINT, Integer
from typing import Annotated
import datetime
from contextlib import asynccontextmanager
from ..config import settings

params = {}

engine = create_async_engine(settings.db.url, echo=False, **params)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@asynccontextmanager
async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

bigint_pk = Annotated[int, mapped_column(BIGINT, primary_key=True)]
int_pk = Annotated[int, mapped_column(Integer, primary_key=True)]
date_pk = Annotated[datetime.datetime, mapped_column(primary_key=True, server_default=text("TIMEZONE('Europe/Moscow', now())"))]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('Europe/Moscow', now())"))]
updated_at = Annotated[
    datetime.datetime, 
    mapped_column(
        server_onupdate=text("TIMEZONE('Europe/Moscow', now())"),
        server_default=text("TIMEZONE('Europe/Moscow', now())"),
    )
]

class Base(DeclarativeBase):
    pass