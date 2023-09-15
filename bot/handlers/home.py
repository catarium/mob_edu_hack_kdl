from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.misc import dp

@dp.message(F.text =='/test')
async def test(message: Message, state: FSMContext):
    await message.answer('hello')
