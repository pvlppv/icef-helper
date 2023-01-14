from aiogram.dispatcher.filters.state import StatesGroup, State


class changeprofile(StatesGroup):
    username = State()
    name = State()
    course = State()
    academic_group = State()
    specialization = State()
    additional_courses = State()
    sport = State()
    email = State()

