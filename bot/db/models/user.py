from typing import List, Optional

from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from bot.db.models.base import Base

Base = declarative_base
class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    lastname: Mapped[str]
    type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_on": 'type',
        "polymorphic_identity": "user"
    }


class Teacher(User):
    __tablename__ = 'teacher'

    teacher_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    class_id = relationship('Class_id', back_populates='classrooms')


class Student(User):
    __tablename__ = 'student'

    stud_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    marks = Column(String)

class ClassRoom:
    __tablename__ = 'classrooms'

    class_id = Column(Integer, primary_key=True, nullable=False)
    class_name = Column(String)
    way_id = relationship('Way_id', back_populates='way')

class Way:
    __tablename__ = 'way'

    Way_id = Column(Integer, primary_key=True, nullable=False)
    way_name = Column(String)

