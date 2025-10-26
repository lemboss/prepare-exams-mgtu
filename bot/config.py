from dataclasses import dataclass
from datetime import datetime
from environs import Env
import logging

@dataclass
class DB:
    host: str
    port: int
    database: str
    user: str
    password: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
    
@dataclass
class TGBot:
    token: str
    admin: str
    
@dataclass
class Settings:
    start_prepare_date: datetime
    last_prepare_date: datetime
    prepare_per_week: int
    
@dataclass
class Config:
    mode: bool
    settings: Settings
    db: DB
    tgbot: TGBot
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    mode = env('MODE')
    if env('MODE') not in ("TEST", "DEV", "PROD"):
        raise Exception
    
    db_prefix = "TEST_" if mode == "TEST" else ""

    start_prepare_date=datetime(year=2025, month=10, day=24)
    last_prepare_date=datetime(year=2026, month=8, day=1)
    prepare_per_week=6
    
    settings = Config(
        mode=mode,
        settings=Settings(
            start_prepare_date=start_prepare_date,
            last_prepare_date=last_prepare_date,
            prepare_per_week=prepare_per_week
        ),
        db=DB(
            host=env(db_prefix+'DB_HOST'),
            port=env(db_prefix+'DB_PORT'),
            database=env(db_prefix+'DB_NAME'),
            user=env(db_prefix+'DB_USER'),
            password=env(db_prefix+'DB_PASS'),
        ),
        tgbot=TGBot(
            token=env("TGBOT_TOKEN"),
            admin=int(env("ADMIN_ID"))
        )
    )
    
    if settings.mode in ("DEV", "TEST"):
        logging.basicConfig(level=logging.DEBUG, #filename="logs.log",filemode="a",
                    format='[%(asctime)s] #%(levelname)-8s %(filename)s:' '%(lineno)d - %(name)s - %(message)s')   
    else:
        logging.basicConfig(level=logging.INFO, filename="./logs/logs.log",filemode="a",
                    format='[%(asctime)s] #%(levelname)-8s %(filename)s:' '%(lineno)d - %(name)s - %(message)s')   
        
    return settings

settings = load_config()