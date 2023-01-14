from aiogram.dispatcher.filters.state import StatesGroup, State


class youtube_search(StatesGroup):
    search = State()