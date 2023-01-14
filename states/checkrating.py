from aiogram.dispatcher.filters.state import StatesGroup, State


class checkrating(StatesGroup):
    text = State()
    answer = State()