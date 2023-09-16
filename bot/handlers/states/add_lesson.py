from aiogram.fsm.state import StatesGroup, State


class AddLessonStateGroup(StatesGroup):
    name = State()
