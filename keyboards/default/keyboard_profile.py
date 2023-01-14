from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_profile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 My profile'),
            KeyboardButton(text='👤 Another profile'),
        ],
        [
            KeyboardButton(text='🔎 Searching by interests')
        ],
        [
            KeyboardButton(text='⬅️ Networking'),
        ]
    ],
    resize_keyboard=True
)

