from aiogram.fsm.state import StatesGroup, State


class AddWayStateGroup(StatesGroup):
    name = State()