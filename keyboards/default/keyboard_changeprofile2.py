from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_changeprofile2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Name'),
        ],
        [
            KeyboardButton(text='👥 Course'),
        ],
        [
            KeyboardButton(text='🫂 Academic group'),
        ],
        [
            KeyboardButton(text='💼 Specialization'),
        ],
        [
            KeyboardButton(text='🔭 Additional courses'),
        ],
        [
            KeyboardButton(text='🎱 Sport'),
        ],
        [
            KeyboardButton(text='🔰 Username'),
        ],
        [
            KeyboardButton(text='⬅️ Profile'),
        ]
    ],
    resize_keyboard=True
)


