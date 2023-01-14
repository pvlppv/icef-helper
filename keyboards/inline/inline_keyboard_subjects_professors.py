from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_subjects_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📘 Calculus professors', callback_data='edit_calculus_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📗 Statistics professors', callback_data='edit_statistics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📙 Microeconomics professors', callback_data='edit_microeconomics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📕 Macroeconomics professors', callback_data='edit_macroeconomics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📔 History professors', callback_data='edit_history_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📒 Philosophy professors', callback_data='edit_philosophy_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📓 ICS professors', callback_data='edit_ics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='files_back'),
                                    ]
                                ])
