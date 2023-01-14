from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_editprofile = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='👤 Name', callback_data='editprofile_name'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📧 Email', callback_data='editprofile_email'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='👥 Course', callback_data='editprofile_course'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🫂 Academic group', callback_data='editprofile_academic_group'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='💼 Specialization', callback_data='editprofile_specialization'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🔭 Additional courses', callback_data='editprofile_additional_courses'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🎱 Sport', callback_data='editprofile_sport'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🔰 Username', callback_data='editprofile_username'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='editprofile_back'),
                                    ],
                                ])