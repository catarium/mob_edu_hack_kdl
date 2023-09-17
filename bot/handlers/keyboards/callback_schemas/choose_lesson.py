from typing import Optional
from aiogram.filters.callback_data import CallbackData


class LessonCallbackFactory(CallbackData, prefix="lesson"):
    class_id: int
    lesson_id: int
