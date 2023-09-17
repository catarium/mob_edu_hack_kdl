from typing import List

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.classroom import ClassroomCRUD
from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.crud.way import LessonCRUD
from bot.db.models.classroom import Classroom
from bot.db.models.user import User, Teacher, Student
from bot.db.models.way import Lesson
from bot.handlers.keyboards.callback_schemas.choose_class import ClassCallbackFactory
from bot.handlers.keyboards.callback_schemas.choose_lesson import LessonCallbackFactory

from bot.handlers.keyboards.choose_class import get_choose_class_keyboard
from bot.handlers.keyboards.choose_lesson import get_choose_lesson_keyboard
from bot.handlers.keyboards.classroom_menu import get_class_menu_keyboard
from bot.handlers.keyboards.lesson_menu import get_lesson_menu_keyboard
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.handlers.states.bind_class import BindClassGroup
from bot.handlers.states.class_menu import ClassMenuGroup
from bot.handlers.states.grades4 import GradesGroup
from bot.misc import dp, session_maker


classroom_crud = ClassroomCRUD(session_maker)
teacher_crud = TeacherCRUD(session_maker)
lesson_crud = LessonCRUD(session_maker)
student_crud = StudentCRUD(session_maker)
@dp.message(F.text == '/class')
async def bind_class(message: Message, state: FSMContext):
    await message.answer('Введите id класса')
    await state.set_state(BindClassGroup.class_id)


@dp.message(BindClassGroup.class_id)
async def class_id_entered(meessage: Message, state: FSMContext):
    student = student_crud.get_by_tg_id(meessage.from_user.id)
    classroom_crud.add_student(int(meessage.text), student.id)
    await state.clear()


@dp.message(F.text == '/program')
async def get_program(message: Message, state: FSMContext):
    student: Student = student_crud.get_by_tg_id(message.from_user.id)
    if not student.classroom:
        print('asdsa;dj')
        return
    lessons_ids = [l.id for l in student.classroom.way.lessons]
    completed_lessons_ids = [l.id for l in student.classroom.completed_lessons]
    msg = []
    for l in student.classroom.way.lessons:
        msg.append(l.name)
        if str(l.id) in student.grades:
            msg.append(str(student.grades[str(l.id)]))
    await message.answer('\n'.join(msg))

