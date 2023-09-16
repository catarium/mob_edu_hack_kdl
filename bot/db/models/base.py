from typing import Any

from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: JSON
    }
