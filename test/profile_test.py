from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, User
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker, with_polymorphic

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student, User

from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.models.user import User
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '5917219823:AAHHUU2XR_Rg6XrwXunhsoq6Y6mVoSS8usU'
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
button_1 = InlineKeyboardButton(text='Расписание')
button_2 = InlineKeyboardButton(text='/prof')
keyboard2 = InlineKeyboardMarkup(inline_keyboard=[[button_2]])
keyboard1 = InlineKeyboardMarkup(inline_keyboard=[[button_1]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='prof')


@dp.message(Command(commands=['prof']))
async def profile(message: Message):
    with Session() as session:
        stmt = select(with_polymorphic(User, [Teacher, Student])).where(User.telegram_id == message.from_user.id)
        user = session.execute(stmt).one_or_none()
    await message.answer(f'Имя: {user[2]}\nФамилия: {user[3]}\nСтатус: {user[4]}', reply_markup=keyboard1)



@dp.message(F.text == 'Расписание')
async def desk(less: list, message: Message):
    await message.answer(text='\n'.join(less), reply_markup=keyboard2)

if __name__ == '__main__':
    dp.run_polling(bot)