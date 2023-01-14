from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/editprofile'),
        ],
        [
            KeyboardButton(text='/updatemenu'),
        ],
        [
            KeyboardButton(text='/report'),
        ],
        [
            KeyboardButton(text='/subscription'),
        ],
        [
            KeyboardButton(text='⬅️ Menu 3'),
        ]
    ],
    resize_keyboard=True
)

kb_settings2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/editprofile'),
        ],
        [
            KeyboardButton(text='/updatemenu'),
        ],
        [
            KeyboardButton(text='/report'),
        ],
        [
            KeyboardButton(text='/subscription'),
        ],
        [
            KeyboardButton(text='/createuser'),
        ],
        [
            KeyboardButton(text='/deleteuser'),
        ],
        [
            KeyboardButton(text='/allusers'),
        ],
        [
            KeyboardButton(text='/editsub'),
        ],
        [
            KeyboardButton(text='/editicefevents'),
        ],
        [
            KeyboardButton(text='/mailing'),
        ],
        [
            KeyboardButton(text='⬅️ Menu 3'),
        ]
    ],
    resize_keyboard=True
)

kb_settings3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/editprofile'),
        ],
        [
            KeyboardButton(text='/updatemenu'),
        ],
        [
            KeyboardButton(text='/report'),
        ],
        [
            KeyboardButton(text='/subscription'),
        ],
        [
            KeyboardButton(text='/changetimetable'),
        ],
        [
            KeyboardButton(text='⬅️ Menu 3'),
        ]
    ],
    resize_keyboard=True
)

