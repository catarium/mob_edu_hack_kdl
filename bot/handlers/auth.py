from sqlalchemy.orm import Session, sessionmaker
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from bot.db.crud.user import UserCRUD, TeacherCRUD, StudentCRUD
from bot.db.models.user import *
from bot.handlers.keyboards.user_type import get_user_type_keyboard
from bot.handlers.states.auth import AuthGroup
from bot.misc import dp, session_maker
from bot.db.models.user import Teacher, Student

session = session_maker(bind="engine")
session = Session()
button1 = InlineKeyboardButton(text='Учитель')
button2 = InlineKeyboardButton(text='Ученик')
keyboard1 = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2]])
@dp.message(CommandStart())
async def reg(message: Message):
    await message.answer('Какой ваш статус', reply_markup=keyboard1)


@dp.message(F.text('Ученик'))
async def teach(message: Message):
    id = message.from_user.id
    # сюда писать ввод id и статуса ученика в бд
    await message.answer('Введите Фамилию и имя через пробел, используя /namest <Имя> <Фамилия>')

@dp.message(F.text('Учитель'))
async def teach(message: Message):
    id = message.from_user.id
    # сюда писать ввод id и статуса учителя в бд
    await message.answer('Введите Фамилию и имя через пробел, используя /namet <Имя> <Фамилия>')


@dp.message(Command(commands=['namet']))
async def name(message: Message):
    name = message.text.split()
    if len(name) < 3:
        await message.answer(f'Неправильный формат ввода')
    else:
        # сюда писать ввод id и статуса учителя в бд
        await message.answer(f'Вы успешно зарегистрированы под именем {name[1:]}')

@dp.message(Command(commands=['namest']))
async def name(message: Message):
    name = message.text.split()
    if len(name) < 3:
        await message.answer(f'Неправильный формат ввода')
    else:
        # сюда писать ввод id и статуса студня в бд
        await message.answer(f'Вы успешно зарегистрированы под именем {name[1:]}')