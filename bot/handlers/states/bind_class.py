from aiogram.fsm.state import StatesGroup, State


class BindClassGroup(StatesGroup):
    class_id = State()
