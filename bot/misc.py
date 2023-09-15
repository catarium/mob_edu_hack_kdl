# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import create_engine

from bot.core.config import config
# from bot.services.auto_news import Notifier

storage = MemoryStorage()
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(storage=storage)


def database_init():
    from bot.db.models.base import Base
    from bot.db.models.user import User, Student, Teacher
    from bot.db.models.classroom import Classroom

    engine = create_engine(f'sqlite:///{config.DB_NAME}')
    Base.metadata.create_all(engine)


# notifier = Notifier(AsyncIOScheduler(), bot)


def setup():
    import bot.handlers.home
    import bot.handlers.auth