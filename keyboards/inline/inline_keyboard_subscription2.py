from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_subscription2 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='💳 Purchase', callback_data='purchase'),
                                    ]
                                ])