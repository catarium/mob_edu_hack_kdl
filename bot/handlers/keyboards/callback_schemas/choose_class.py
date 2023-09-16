from typing import Optional
from aiogram.filters.callback_data import CallbackData


class ClassCallbackFactory(CallbackData, prefix="way"):
    class_id: int
