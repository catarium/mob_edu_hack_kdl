# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot.core.config import config
# from bot.services.auto_news import Notifier

storage = MemoryStorage()
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(storage=storage)


engine = create_engine(f'sqlite:///{config.DB_NAME}', echo=True)
session_maker = sessionmaker(engine)


def database_init():
    print('creating tables')
    from bot.db.models.base import Base
    from bot.db.models.user import User, Student, Teacher
    from bot.db.models.classroom import Classroom
    from bot.db.models.way import Way, Lesson
    from bot.db.models.classroom_lesson import association_table

    Base.metadata.create_all(engine)


# notifier = Notifier(AsyncIOScheduler(), bot)


def setup():
    import bot.handlers.home
    import bot.handlers.auth
    import bot.handlers.teacher_classroom
    import bot.handlers.create_classroom
    import bot.handlers.create_way
    import bot.handlers.student_class
