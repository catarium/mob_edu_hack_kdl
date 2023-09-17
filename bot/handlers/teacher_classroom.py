from typing import List

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.classroom import ClassroomCRUD
from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.crud.way import LessonCRUD
from bot.db.models.classroom import Classroom
from bot.db.models.user import User, Teacher
from bot.db.models.way import Lesson
from bot.handlers.keyboards.callback_schemas.choose_class import ClassCallbackFactory
from bot.handlers.keyboards.callback_schemas.choose_lesson import LessonCallbackFactory

from bot.handlers.keyboards.choose_class import get_choose_class_keyboard
from bot.handlers.keyboards.choose_lesson import get_choose_lesson_keyboard
from bot.handlers.keyboards.classroom_menu import get_class_menu_keyboard
from bot.handlers.keyboards.lesson_menu import get_lesson_menu_keyboard
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.handlers.states.class_menu import ClassMenuGroup
from bot.handlers.states.grades4 import GradesGroup
from bot.misc import dp, session_maker


classroom_crud = ClassroomCRUD(session_maker)
teacher_crud = TeacherCRUD(session_maker)
lesson_crud = LessonCRUD(session_maker)
student_crud = StudentCRUD(session_maker)


@dp.callback_query(F.data == 'classes_list')
async def classes_list(call: CallbackQuery, state: FSMContext):
    await call.answer()
    print()
    teacher: Teacher = teacher_crud.get_by_tg_id(call.from_user.id)
    msg = 'Выберите класс'
    await call.message.answer(msg, reply_markup=get_choose_class_keyboard(teacher.classes))


@dp.callback_query(ClassCallbackFactory.filter())
async def class_menu(call: CallbackQuery, callback_data: ClassCallbackFactory, state: FSMContext):
    teacher = teacher_crud.get_by_tg_id(call.from_user.id)
    classroom: Classroom = classroom_crud.get_by_id(callback_data.class_id)
    msg = f'''
Имя класса: {classroom.name}
id класса: {classroom.id}
Количество участников: {len(classroom.students)}
    '''
    await call.message.answer(msg, reply_markup=get_class_menu_keyboard())
    await state.set_state(ClassMenuGroup.active)
    await state.update_data(class_id=classroom.id)


@dp.callback_query(F.data == 'program_menu', ClassMenuGroup.active)
async def program_menu(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    classroom: Classroom = classroom_crud.get_by_id(data['class_id'])
    await call.message.answer('Список уроков', reply_markup=get_choose_lesson_keyboard(classroom))


@dp.callback_query(LessonCallbackFactory.filter())
async def lesson_menu(call: CallbackQuery, callback_data: LessonCallbackFactory, state: FSMContext):
    await call.answer()
    lesson: Lesson = lesson_crud.get_by_id(callback_data.lesson_id)
    classroom: Classroom = classroom_crud.get_by_id(callback_data.class_id)
    if lesson.id in [l.id for l in classroom.completed_lessons]:
        status = 'Завершен'
    else:
        status = 'Не завершен'
    msg = f'''
Имя урока: {lesson.name}
Статус: {status}    
'''
    await call.message.answer(msg, reply_markup=get_lesson_menu_keyboard())
    await state.update_data(lesson_id=lesson.id)


@dp.callback_query(F.data == 'change_lesson_status')
async def change_lesson_status(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lesson = lesson_crud.get_by_id(data['lesson_id'])
    classroom = classroom_crud.get_by_id(data['class_id'])
    classroom_crud.change_lesson_status(classroom, lesson)
    await lesson_menu(call, LessonCallbackFactory(class_id=classroom.id, lesson_id=lesson.id), state)


@dp.callback_query(F.data == 'set_grades')
async def set_grades(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lesson = lesson_crud.get_by_id(data['lesson_id'])
    classroom = classroom_crud.get_by_id(data['class_id'])
    msg = '\n'.join([f'{s.id} {s.name} {s.lastname}' for s in classroom.students])
    await call.message.answer(msg)
    await call.message.answer('Введите id ученика')
    await state.set_state(GradesGroup.student_id)


@dp.message(GradesGroup.student_id)
async def student_id_entered(message: Message, state: FSMContext):
    await state.update_data(student_id=message.text)
    await state.set_state(GradesGroup.grade)
    await message.answer('Введите оценку')


@dp.message(GradesGroup.grade)
async def grade_entered(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    data = await state.get_data()
    student = student_crud.get_by_id(int(data['student_id']))
    await student_crud.add_grade(int(student.id), data['lesson_id'], message.text)
    await state.set_state(ClassMenuGroup.active)

