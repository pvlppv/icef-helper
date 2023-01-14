from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_skipregistration = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💨 Skip'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


