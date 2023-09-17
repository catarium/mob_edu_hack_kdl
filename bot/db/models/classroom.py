from typing import List

from sqlalchemy import Column, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column

from bot.db.models.base import Base
from bot.db.models.classroom_lesson import association_table
from bot.db.models.user import Student





class Classroom(Base):
    __tablename__ = 'classroom'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    way_id: Mapped[int] = mapped_column(ForeignKey('way.id'))
    way: Mapped['Way'] = relationship(back_populates='classes',
                                      foreign_keys=[way_id],
                                      lazy='selectin')
    teacher_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    teacher: Mapped['Teacher'] = relationship(back_populates="classes",
                                              foreign_keys=[teacher_id])
    students: Mapped[List['Student']] = relationship(back_populates='classroom',
                                                     cascade='all, delete-orphan',
                                                     foreign_keys="Student.classroom_id",
                                                     lazy='selectin')
    completed_lessons: Mapped[List['Lesson']] = relationship(back_populates='classrooms',
                                                   secondary=association_table,
                                                     lazy='selectin')

