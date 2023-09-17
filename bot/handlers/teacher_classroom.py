from typing import List

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.classroom import ClassroomCRUD
from bot.db.crud.user import UserCRUD, TeacherCRUD
from bot.db.models.classroom import Classroom
from bot.db.models.user import User, Teacher
from bot.handlers.keyboards.callback_schemas.choose_class import ClassCallbackFactory

from bot.handlers.keyboards.choose_class import get_choose_class_keyboard
from bot.handlers.keyboards.classroom_menu import get_class_menu_keyboard
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker


classroom_crud = ClassroomCRUD(session_maker)
teacher_crud = TeacherCRUD(session_maker)


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



