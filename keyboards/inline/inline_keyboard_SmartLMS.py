from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from loader import db_sql

ikb_SmartLMS = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📚 Subjects', callback_data='SmartLMS_subjects'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🕓 Timetable', callback_data='SmartLMS_timetable'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='👨🏼‍🏫 Office hours', callback_data='SmartLMS_officehours'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='🔭 Optional courses', callback_data='SmartLMS_optionalcourses'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📖 Exams timetable', callback_data='SmartLMS_examstimetable'),
                                    ]
                                ])

ikb_SmartLMS_subjects = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus', callback_data='SmartLMS_subjects_calculus'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics', callback_data='SmartLMS_subjects_statistics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics', callback_data='SmartLMS_subjects_microeconomics'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History', callback_data='SmartLMS_subjects_history'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📒 Philosophy', callback_data='files_philosophy'),
                                    # ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    # [
                                    #     InlineKeyboardButton(text='📓 ICS', callback_data='files_ics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_calculus = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus', callback_data='SmartLMS_subjects_calculus_back'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Lectures', callback_data='SmartLMS_subjects_calculus_classes'),
                                        InlineKeyboardButton(text='HA', callback_data='SmartLMS_subjects_calculus_ha'),
                                        InlineKeyboardButton(text='Other', callback_data='SmartLMS_subjects_calculus_other')
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics', callback_data='SmartLMS_subjects_statistics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics', callback_data='SmartLMS_subjects_microeconomics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History', callback_data='SmartLMS_subjects_history'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_statistics = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus', callback_data='SmartLMS_subjects_calculus'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics', callback_data='SmartLMS_subjects_statistics_back'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Lectures', callback_data='SmartLMS_subjects_statistics_classes'),
                                        InlineKeyboardButton(text='HA', callback_data='SmartLMS_subjects_statistics_ha'),
                                        InlineKeyboardButton(text='Other', callback_data='SmartLMS_subjects_statistics_other')
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics', callback_data='SmartLMS_subjects_microeconomics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History', callback_data='SmartLMS_subjects_history'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_microeconomics = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus', callback_data='SmartLMS_subjects_calculus'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics', callback_data='SmartLMS_subjects_statistics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics', callback_data='SmartLMS_subjects_microeconomics_back'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Lectures', callback_data='SmartLMS_subjects_microeconomics_classes'),
                                        InlineKeyboardButton(text='HA', callback_data='SmartLMS_subjects_microeconomics_ha'),
                                        InlineKeyboardButton(text='Other', callback_data='SmartLMS_subjects_microeconomics_other')
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History', callback_data='SmartLMS_subjects_history'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_history = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus', callback_data='SmartLMS_subjects_calculus'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics', callback_data='SmartLMS_subjects_statistics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics', callback_data='SmartLMS_subjects_microeconomics'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History', callback_data='SmartLMS_subjects_history_back'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Lectures', callback_data='SmartLMS_subjects_history_classes'),
                                        InlineKeyboardButton(text='HA', callback_data='SmartLMS_subjects_history_ha'),
                                        InlineKeyboardButton(text='Other', callback_data='SmartLMS_subjects_history_other')
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_timetable = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='✔️ Send', callback_data='SmartLMS_timetable_timetable_show'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_officehours = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='✔️ Send', callback_data='SmartLMS_timetable_officehours_show'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_optionalcourses = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='✔️ Send', callback_data='SmartLMS_timetable_optionalcourses_show'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_examstimetable = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='✔️ Send', callback_data='SmartLMS_timetable_examstimetable_show'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])