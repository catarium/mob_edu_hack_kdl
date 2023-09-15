from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.models.user import User
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker


teacher_crud = TeacherCRUD(session_maker)
student_crud = StudentCRUD(session_maker)


@dp.callback_query(F.data == 'type_teacher')
async def teacher_auth(call: CallbackQuery, state: FSMContext):
    await state.update_data(type='teacher')
    await state.set_state(AuthGroup.name)
    await call.message.answer('Введите имя')


@dp.message(AuthGroup.name)
async def name_entered(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AuthGroup.lastname)
    await message.answer('Введите фамилию')


@dp.message(AuthGroup.lastname)
async def lastname_entered(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text)
    await state.update_data(telegram_id=message.from_user.id)
    data = await state.get_data()
    if data['type'] == 'teacher':
        print(teacher_crud.create(**data))
    elif data['type'] == 'student':
        student_crud.create(**data)
