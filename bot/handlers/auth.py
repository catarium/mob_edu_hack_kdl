from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.models.user import *
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker
from bot.db.models.user import Teacher, Student

button1 = InlineKeyboardButton(text='Учитель')
button2 = InlineKeyboardButton(text='Ученик')
keyboard1 = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2]])
@dp.message(CommandStart())
async def reg(message: Message):
    await message.answer('Какой ваш статус', reply_markup=keyboard1)

@dp.message(F.text('Учитель'))
async def teach(message: Message):
    await async