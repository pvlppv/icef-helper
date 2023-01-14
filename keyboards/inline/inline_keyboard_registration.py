from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_registration = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Register', callback_data='register'),
                                    ]
                                ])