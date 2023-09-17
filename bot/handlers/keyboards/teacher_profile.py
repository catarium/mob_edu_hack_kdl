from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_teacher_profile_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Мои классы", callback_data="classes_list")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, )
    return keyboard
