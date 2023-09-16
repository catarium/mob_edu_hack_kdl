from typing import List

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from bot.db.models.base import Base
from bot.db.models.user import Student


class Way(Base):
    __tablename__ = 'way'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    teacher_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    teacher: Mapped['Teacher'] = relationship(back_populates="ways",
                                              foreign_keys=[teacher_id])
    classes: Mapped[List['Classroom']] = relationship(back_populates='way',
                                                   cascade='all, delete-orphan',
                                                   foreign_keys="Classroom.way_id")
    lessons: Mapped[List['Lesson']] = relationship(back_populates='way',
                                                     cascade='all, delete-orphan',
                                                     foreign_keys="Lesson.way_id")


class Lesson(Base):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    way_id: Mapped[int] = mapped_column(ForeignKey('way.id'))
    way: Mapped['Way'] = relationship(back_populates='lessons',
                                      foreign_keys=[way_id])



