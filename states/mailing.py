from aiogram.dispatcher.filters.state import StatesGroup, State


class mailing(StatesGroup):
    text = State()
    state = State()
    photo = State()