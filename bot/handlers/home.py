from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '5917219823:AAHHUU2XR_Rg6XrwXunhsoq6Y6mVoSS8usU'
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)

button_1 = InlineKeyboardButton(text='Расписание')
keyboard = InlineKeyboardMarkup(keyboard=[[button_1]])

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='prof')
@dp.message(Command(command=['prof']))
async def profile(link: str, name: str, surname: str, status: str, points: int, classes: list, message: Message):
    if status == 'Ученик':
        cap = f'Имя: {name}\nФамилия: {surname}\nБаллы: {points}'
    else:
        cap = f'Имя: {name}\nФамилия: {surname}\nКлассы:\n' + '\n'.join(classes)
    await message.send_photo(message.from_user.id, photo=link, caption=cap, reply_markup=keyboard)

@dp.message(F.text == 'Расписание')
async def desk(less: list, message: Message):
    await message.answer(text='\n'.join(less))

if __name__ == '__main__':
    dp.run_polling(bot)
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.misc import dp

@dp.message(F.text =='/test')
async def test(message: Message, state: FSMContext):
    await message.answer('hello')

@dp.message(F.text == '/start')
async def home(message: Message, state: FSMContext):
    print(message.from_user.id)


button_1 = InlineKeyboardButton(text='Расписание')
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='prof')
    id = message.from_user.id



@dp.message(Command(commands=['prof']))
async def profile(link: str = 'State\photo.jpg', name: str = 'Лёха', surname: str = 'Med', status: str = 'Stud',\
                  points: int = 5, classes: list = ['11A'], message ):
    if status == 'Ученик':
        cap = f'Имя: {name}\nФамилия: {surname}\nБаллы: {points}'
    else:
        cap = f'Имя: {name}\nФамилия: {surname}\nКлассы:\n' + '\n'.join(classes)
    await bot.send_photo(message.from_user.id, photo=link, caption=cap, reply_markup=keyboard)


@dp.message(F.text == 'Расписание')
async def desk(less: list, message: Message):
    await message.answer(text='\n'.join(less))
