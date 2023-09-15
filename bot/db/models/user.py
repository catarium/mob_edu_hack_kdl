from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db.models.base import Base


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
    classes: Mapped[List['Classroom']] = relationship(back_populates='teacher',
                                                     cascade='all, delete-orphan',
                                                      foreign_keys='Classroom.teacher_id')
    __mapper_args__ = {
        "polymorphic_identity": "teacher"
    }


class Student(User):
    rating: Mapped[int] = mapped_column(default=0)
    classroom_id: Mapped[Optional[int]] = mapped_column(ForeignKey('classroom.id'))
    classroom: Mapped[Optional['Classroom']] = relationship(back_populates='',
                                                        foreign_keys=[classroom_id])
    __mapper_args__ = {
        "polymorphic_identity": "student"
    }
