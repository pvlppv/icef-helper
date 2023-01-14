from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_ICEFHelperMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌐 ICEF Helper'),
        ],
        [
            KeyboardButton(text='⬅️ Networking'),
            KeyboardButton(text='NOT ICEF'),
            KeyboardButton(text='Studying ➡️')
        ]
    ],
    resize_keyboard=True,
)

kb_noticef = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='NOT ICEF'),
        ],
        [
            KeyboardButton(text='✏️ Notes'),
            KeyboardButton(text='🕓 Notifications'),
            KeyboardButton(text='📟 Study Search')
        ],
        [
            KeyboardButton(text='⬇️ Home'),
        ]
    ],
    resize_keyboard=True,
)

kb_networking = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Profile'),
        ],
        [
            KeyboardButton(text='🗣 Network'),
            KeyboardButton(text='🗞 News'),
            KeyboardButton(text='🎫 Events'),
            KeyboardButton(text='💋 Anonchat')
        ],
        [
            KeyboardButton(text='Home ➡️'),
        ]
    ],
    resize_keyboard=True
)

kb_studying = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💠 Smart LMS'),
        ],
        [
            KeyboardButton(text='🗓️ Schedule'),
            KeyboardButton(text='👨🏻‍🏫 Professors'),
            KeyboardButton(text='🗃 Handbook'),
            KeyboardButton(text='📂 Materials'),
            KeyboardButton(text='🚪 Locations')
        ],
        [
            KeyboardButton(text='⬅️ Home'),
        ]
    ],
    resize_keyboard=True
)
