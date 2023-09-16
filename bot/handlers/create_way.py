from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.models.user import User, Teacher
from bot.handlers.keyboards.add_lesson import get_add_lesson_keyboard
from bot.handlers.keyboards.choose_way import get_choose_way_keyboard
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.add_class import AddClassStateGroup
from bot.handlers.states.add_lesson import AddLessonStateGroup
from bot.handlers.states.add_way import AddWayStateGroup
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker


teacher_crud = TeacherCRUD(session_maker)
student_crud = StudentCRUD(session_maker)


@dp.callback_query(F.data == 'add_way')
async def add_way(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(AddWayStateGroup.name)
    await call.message.answer('Введите имя программы')


@dp.message(AddWayStateGroup.name)
async def way_name_entered(message: Message, state: FSMContext):
    data = await state.get_data()
    data['way'] = {'name': message.text, 'lessons': []}
    await state.set_data(data)
    await state.set_state(AddLessonStateGroup.name)
    await message.answer('Введите имя урока',)


@dp.message(AddLessonStateGroup.name)
async def lesson_name_entered(message: Message, state: FSMContext):
    data = await state.get_data()
    data['way']['lessons'].append({"name": message.text})
    await state.set_data(data)
    await message.answer('Введите имя урока',
                         reply_markup=get_add_lesson_keyboard())
