from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_lesson_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Сменить статус", callback_data="change_lesson_status")],
        [InlineKeyboardButton(text='Выставить оценки', callback_data="set_grades")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
