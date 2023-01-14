from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_materials = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Books', url='https://drive.google.com/drive/folders/1JqfU-xubOSG-9RdEBWlwnSbWWTZABpm7'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='ICEF past exams', url='https://drive.google.com/drive/folders/1AA3FPxFm7jOKJFN2mAi3fjiPR0ZgAbhG'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Custom content', url='https://drive.google.com/drive/folders/1m-9D5vGWsR7ydgVCO1qFCBig9084MmLC'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Career materials', url='https://drive.google.com/drive/folders/1HeMXUe0HHl-WdS4BqX6dJAyJOBbGP2t1'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='UoL 2003-2017', url='https://drive.google.com/drive/folders/1sML4jKYIWvxf8gk0a-D5mtToDjykZWOj'),
                                    ]
                                ])