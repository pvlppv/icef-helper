from aiogram.dispatcher.filters.state import StatesGroup, State


class registration(StatesGroup):
    user_id = State()
    name = State()
    username = State()
    course = State()
    academic_group = State()
    english_group = State()
    specialization = State()
    additional_cources = State()
    sport = State()
    email = State()

class accept_registration(StatesGroup):
    user_id = State()

class decline_registration(StatesGroup):
    user_id = State()





