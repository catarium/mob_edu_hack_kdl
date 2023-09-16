from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.models.classroom import Classroom
from bot.handlers.keyboards.callback_schemas.choose_class import \
    ClassCallbackFactory


def get_choose_class_keyboard(classes: List[Classroom]):
    builder = InlineKeyboardBuilder()
    for classroom in classes:
        builder.button(text=classroom.name,
                       callback_data=ClassCallbackFactory(class_id=classroom.id))
    builder.row(InlineKeyboardButton(text='Создать новый', callback_data='add_class'))
    return builder.as_markup()
