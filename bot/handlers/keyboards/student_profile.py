from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_student_profile_keyboard():
    buttons = [
        [KeyboardButton(text="/program")],
        [KeyboardButton(text="/class")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard
