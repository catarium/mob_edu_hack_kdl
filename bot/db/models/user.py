from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    telgram_id: Mapped[str]
    name: Mapped[str]
    lastname: Mapped[str]
    type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_on": 'type',
        "polymorphic_identity": "user"
    }


class Teacher(User):
    classes: Mapped[List['Class']] = relationship(back_populates='teacher',
                                                     cascade='all, delete-orphan')
    __mapper_args__ = {
        "polymorphic_identity": "teacher"
    }


class Student(User):
    class_: Mapped['Class'] = relationship(back_populates='')
    __mapper_args__ = {
        "polymorphic_identity": "student"
    }
