from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1️⃣ course'),
            KeyboardButton(text='2️⃣ course')
        ],
        [
            KeyboardButton(text='3️⃣ course'),
            KeyboardButton(text='4️⃣ course')
        ]
    ],
    resize_keyboard=True
)


