from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_schedule_subjects = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📘 Calculus', callback_data='schedule_calculus'),
        ],
        [
            InlineKeyboardButton(text='📗 Statistics', callback_data='schedule_statistics'),
        ],
        [
            InlineKeyboardButton(text='📙 Microeconomics', callback_data='schedule_microeconomics'),
        ],
        [
            InlineKeyboardButton(text='📔 History', callback_data='schedule_history'),
        ],
        [
            InlineKeyboardButton(text='📒 Philosophy', callback_data='schedule_philosophy'),
        ],
        [
            InlineKeyboardButton(text='📓 ICS', callback_data='schedule_ics'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_back'),
        ]
    ])

ikb_schedule_calculus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_calculus_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_calculus_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_calculus_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_calculus_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_calculus_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_calculus_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])

ikb_schedule_statistics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_statistics_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_statistics_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_statistics_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_statistics_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_statistics_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_statistics_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])

ikb_schedule_microeconomics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_microeconomics_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_microeconomics_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_microeconomics_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_microeconomics_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_microeconomics_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_microeconomics_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])

ikb_schedule_history = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_history_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_history_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_history_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_history_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_history_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_history_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])

ikb_schedule_philosophy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_philosophy_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_philosophy_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_philosophy_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_philosophy_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_philosophy_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_philosophy_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])

ikb_schedule_ics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕓 Monday', callback_data='schedule_ics_monday'),
            InlineKeyboardButton(text='🕓 Tuesday', callback_data='schedule_ics_tuesday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Wednesday', callback_data='schedule_ics_wednesday'),
            InlineKeyboardButton(text='🕓 Thursday', callback_data='schedule_ics_thursday'),
        ],
        [
            InlineKeyboardButton(text='🕓 Friday', callback_data='schedule_ics_friday'),
            InlineKeyboardButton(text='🕓 Saturday', callback_data='schedule_ics_saturday'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_subjects_back'),
        ]
    ])


