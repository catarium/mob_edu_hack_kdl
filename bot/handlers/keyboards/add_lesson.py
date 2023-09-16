from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_add_lesson_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Готово", callback_data="end_add_lesson")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
