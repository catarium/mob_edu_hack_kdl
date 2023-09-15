from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db.crud.user import UserCRUD
from bot.db.models.user import User
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker


user_crud = UserCRUD(session_maker)

@dp.message(F.text =='/test')
async def test(message: Message, state: FSMContext):
    await message.answer('hello')


@dp.message(F.text == '/start')
async def home(message: Message, state: FSMContext):
    user = user_crud.get_user_by_tg_id(message.from_user.id)
    if not user:
        await message.answer('Кто вы?', reply_markup=get_user_type_keyboard())
    elif user.type == 'teacher':
        pass
    elif user.type == 'student':
        pass




async def teacher_home():
    pass


async def student_home():
    pass
