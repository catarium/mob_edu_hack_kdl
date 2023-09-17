from typing import List

from sqlalchemy import Column, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column

from bot.db.models.base import Base
from bot.db.models.user import Student


association_table = Table(
    "association_table",
    Base.metadata,
    Column("classroom_id", ForeignKey("classroom.id"), primary_key=True),
    Column("lesson_id", ForeignKey("lesson.id"), primary_key=True),
)