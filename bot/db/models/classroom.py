from typing import List

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import Mapped, relationship, mapped_column

from bot.db.models.base import Base


class Classroom(Base):
    __tablename__ = 'classroom'

    id: Mapped[int] = mapped_column(primary_key=True)
    teacher: Mapped['Teacher'] = relationship(back_populates="classes")
    students: Mapped[List['Student']] = relationship(back_populates='class_',
                                                     cascade='all, delete-orphan')
