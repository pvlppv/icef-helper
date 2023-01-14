from aiogram.dispatcher.filters.state import StatesGroup, State


class notifications(StatesGroup):
    text = State()
    date = State()



