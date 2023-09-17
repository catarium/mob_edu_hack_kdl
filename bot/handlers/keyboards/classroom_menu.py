from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_class_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Программа", callback_data="program_menu")],
        [InlineKeyboardButton(text='Создать объявление', callback_data="send_news")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
