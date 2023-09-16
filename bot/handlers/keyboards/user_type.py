from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_user_type_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Учитель", callback_data="type_teacher")],
        [InlineKeyboardButton(text='Ученик', callback_data="type_student")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
