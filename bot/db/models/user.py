from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    lastname = Column(Text)

    __mapper_args__ = {
        "polymorphic_on": True,
        "polymorphic_identity": "user"
    }


class Teacher(User):
    __mapper_args__ = {
        "polymorphic_identity": "teacher"
    }


class Student(User):
    __mapper_args__ = {
        "polymorphic_identity": "student"
    }
