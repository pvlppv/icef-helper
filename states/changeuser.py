from aiogram.dispatcher.filters.state import StatesGroup, State


class createuser(StatesGroup):
    user_id = State()
    username = State()
    name = State()
    course = State()
    academic_group = State()
    english_group = State()

class deleteuser(StatesGroup):
    name = State()

class updateuser(StatesGroup):
    created_at = State()