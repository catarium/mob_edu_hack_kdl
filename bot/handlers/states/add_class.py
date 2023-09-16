from aiogram.fsm.state import StatesGroup, State


class AddClassStateGroup(StatesGroup):
    name = State()
    way = State()

