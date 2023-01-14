from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_professors_info = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus professors', callback_data='SmartLMS_calculus_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics professors', callback_data='SmartLMS_statistics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics professors', callback_data='SmartLMS_microeconomics_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History professors', callback_data='SmartLMS_history_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📒 Philosophy professors', callback_data='SmartLMS_philosophy_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='📓 ICS professors', callback_data='SmartLMS_ics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_SmartLMS_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus professors', callback_data='SmartLMS_calculus_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics professors', callback_data='SmartLMS_statistics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics professors', callback_data='SmartLMS_microeconomics_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History professors', callback_data='SmartLMS_history_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📒 Philosophy professors', callback_data='SmartLMS_philosophy_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='📓 ICS professors', callback_data='SmartLMS_ics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_back'),
                                    ]
                                ])

ikb_SmartLMS_professors_back = InlineKeyboardMarkup(row_width=1,
                                                    inline_keyboard=[
                                                        [
                                                            InlineKeyboardButton(text='⬅️ Back', callback_data='SmartLMS_professors_back')
                                                        ]
                                                    ])

ikb_professors_schedule = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'📘 Calculus professors', callback_data='calculus_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📗 Statistics professors', callback_data='statistics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'📙 Microeconomics professors', callback_data='microeconomics_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'📔 History professors', callback_data='history_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📒 Philosophy professors', callback_data='philosophy_professors'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='📓 ICS professors', callback_data='ics_professors'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='schedule_back'),
                                    ]
                                ])

ikb_calculus_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Патрик Анатолий Евгеньевич', callback_data='calculus_professors_patrik'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Жуков Павел Владимирович', callback_data='calculus_professors_zhukov'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Ворчик Андрей Денисович', callback_data='calculus_professors_vorchik'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'Лукьянченко Пётр Павлович', callback_data='calculus_professors_luk'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Брыков Вячеслав Вячеславович', callback_data='calculus_professors_brikov'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='Шелике Аяна Георгиевна', callback_data='calculus_professors_shelike'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Хассан Яна Нибаль', callback_data='calculus_professors_hassan'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_statistics_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Патрик Анатолий Евгеньевич', callback_data='calculus_professors_patrik'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Люлько Ярослав Александрович', callback_data='statistics_professors_lyulko'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Шелике Аяна Георгиевна', callback_data='calculus_professors_shelike'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'Житлухин Михаил Валентинович', callback_data='statistics_professors_zhitlukhin'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Потапов Денис Игоревич', callback_data='statistics_professors_potapov'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_microeconomics_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Юрко Анна Вячеславовна', callback_data='microeconomics_professors_yurko'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Ворчик Андрей Денисович', callback_data='calculus_professors_vorchik'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Автономов Юрий Владимирович', callback_data='microeconomics_professors_avtonomov'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='📕 Macroeconomics', callback_data='files_macroeconomics'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text=f'Верем Ирина Юрьевна', callback_data='microeconomics_professors_verem'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Векилян Армине Вегенаковна', callback_data='microeconomics_professors_vekilyan'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='🇬🇧 English', callback_data='files_english'),
                                    # ],
                                    [
                                        InlineKeyboardButton(text='Чернышова Яна Алексеевна', callback_data='microeconomics_professors_chernyshova'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Зимрутян Гаянэ Аршаковна', callback_data='microeconomics_professors_zimrutyan'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_history_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Царева Александра Петровна', callback_data='history_professors_tsareva'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Отдельнов Марк Михайлович', callback_data='history_professors_otdelnov'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Петрова Мария Святославовна', callback_data='history_professors_petrova'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_philosophy_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Сейрсингх Кристер Раджендра', callback_data='philosophy_professors_seir'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Отдельнов Марк Михайлович', callback_data='history_professors_otdelnov'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])

ikb_ics_professors = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'Акиншин Анатолий Анатольевич', callback_data='ics_professors_akinshin'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'Бессонова Ирина Анатольевна', callback_data='ics_professors_bessonova'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️ Back', callback_data='professors_back'),
                                    ]
                                ])