from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_anonimchat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔎 Search'),
            KeyboardButton(text='🚫 Exit')
        ]
    ],
    resize_keyboard=True
)

kb_anonimchat1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🕳 Leave'),
        ]
    ],
    resize_keyboard=True
)

kb_anonimchat2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚫 Exit'),
        ]
    ],
    resize_keyboard=True
)

