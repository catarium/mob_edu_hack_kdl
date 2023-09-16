from typing import List

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from bot.db.models.base import Base
from bot.db.models.user import Student

