from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.db.models.classroom import Classroom
from bot.db.models.way import Lesson
from bot.handlers.keyboards.callback_schemas.choose_class import \
    ClassCallbackFactory
from bot.handlers.keyboards.callback_schemas.choose_lesson import LessonCallbackFactory


def get_choose_lesson_keyboard(classroom):
    builder = InlineKeyboardBuilder()
    for lesson in classroom.way.lessons:
        if lesson in classroom.completed_lessons:
            builder.button(text=f'{lesson.name} (завершен)',
                           callback_data=LessonCallbackFactory(class_id=classroom.id, lesson_id=lesson.id))
        else:
            builder.button(text=f'{lesson.name}',
                           callback_data=LessonCallbackFactory(class_id=classroom.id, lesson_id=lesson.id))
    return builder.as_markup()