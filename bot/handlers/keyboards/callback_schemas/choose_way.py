from typing import Optional
from aiogram.filters.callback_data import CallbackData


class WayCallbackFactory(CallbackData, prefix="way"):
    way_id: int
