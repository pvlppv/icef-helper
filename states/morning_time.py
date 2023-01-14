from aiogram.dispatcher.filters.state import StatesGroup, State


class morning_time(StatesGroup):
    time = State()
