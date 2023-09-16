from typing import Optional

from aiogram import F
from aiogram.filters import or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.classroom import ClassroomCRUD
from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.crud.way import WayCRUD, LessonCRUD
from bot.db.models.user import User, Teacher
from bot.handlers.keyboards.callback_schemas.choose_way import \
    WayCallbackFactory
from bot.handlers.keyboards.choose_way import get_choose_way_keyboard
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.add_class import AddClassStateGroup
from bot.handlers.states.add_lesson import AddLessonStateGroup
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker


teacher_crud = TeacherCRUD(session_maker)
student_crud = StudentCRUD(session_maker)
classroom_crud = ClassroomCRUD(session_maker)
way_crud = WayCRUD(session_maker)
lesson_crud = LessonCRUD(session_maker)


@dp.callback_query(F.data == 'add_class')
async def add_class(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(AddClassStateGroup.name)
    await call.message.answer('Введите имя класса')


@dp.message(AddClassStateGroup.name)
async def class_name_entered(message: Message, state: FSMContext):
    teacher: Teacher = teacher_crud.get_by_tg_id(message.from_user.id)
    data = {
        'name': message.text,
    }
    ways = []
    if teacher.ways:
        ways = teacher.ways
    await state.set_data(data)
    await message.answer('Ввыберите программу',
                         reply_markup=get_choose_way_keyboard(ways))


@dp.callback_query(or_f(F.data == 'end_add_lesson', WayCallbackFactory.filter()))
async def the_end(call: CallbackQuery, state: FSMContext, callback_data: Optional[WayCallbackFactory] = None):
    await call.answer()
    data = await state.get_data()
    teacher: Teacher = teacher_crud.get_by_tg_id(call.from_user.id)
    if callback_data:
        way_id = callback_data.way_id
    elif isinstance(data['way'], dict):
        way_id = way_crud.create(name=data['way']['name'], teacher=teacher).id
        lessons = [lesson_crud.create(name=ls['name'], way_id=way_id)
                   for ls in data['way']['lessons']]
    classroom = classroom_crud.create(name=data['name'], teacher=teacher, way_id=way_id)
    await state.clear()
    await call.message.answer('Класс создан')

