from aiogram.fsm.state import StatesGroup, State


class GradesGroup(StatesGroup):
    student_id = State()
    grade = State()
