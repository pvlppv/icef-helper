from aiogram.dispatcher.filters.state import StatesGroup, State


class get_media(StatesGroup):
    file = State()
