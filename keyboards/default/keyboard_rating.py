from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_rating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏆 My rating'),
            KeyboardButton(text='🏆 Another rating'),
        ],
        [
            KeyboardButton(text='⬅️ Back'),
        ]
    ],
    resize_keyboard=True
)


