from aiogram.dispatcher.filters.state import StatesGroup, State


class checkprofile(StatesGroup):
    text = State()
    answer = State()