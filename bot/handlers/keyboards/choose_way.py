from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.models.way import Way
from bot.handlers.keyboards.callback_schemas.choose_way import \
    WayCallbackFactory


def get_choose_way_keyboard(ways: List[Way]):
    builder = InlineKeyboardBuilder()
    for way in ways:
        builder.button(text=way.name,
                       callback_data=WayCallbackFactory(way_id=way.id))
    builder.row(InlineKeyboardButton(text='Создать новую', callback_data='add_way'))
    return builder.as_markup()
