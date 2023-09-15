from sqlalchemy import create_engine

from bot.core.config import config
from bot.db.models.base import Base
from bot.db.models.user import User, Teacher, Student
from bot.db.models.classroom import Classroom

engine = create_engine(f'sqlite:///{config.DB_NAME}', echo=True)

Base.metadata.create_all(engine)