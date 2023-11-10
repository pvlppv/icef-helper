# import os
#
# from aiogram import types
#
# from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, IsSubscriberChannelMessage
# from keyboards.default.keyboard_subjects import kb_subjects, kb_calculus2, kb_statistics2, kb_microeconomics2, kb_macroeconomics2, kb_history2, kb_philosophy2, kb_info2
# # from keyboards.inline.inline_keyboard_allthemes import ikb_allthemes_calculus
# from keyboards.default.keyboard_subjects2 import kb_calculus3, kb_statistics3, kb_microeconomics3, kb_history3, kb_philosophy3, kb_ics3, kb_macroeconomics3
# from loader import dp
# from utils.misc import rate_limit
#
#
# @rate_limit(limit=3, key='📚 Subjects')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📚 Subjects')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📚 Subjects:</b>',
#                          reply_markup=kb_subjects)
#     # await message.answer(f'<b>📚 Subjects:</b>',
#     #                      reply_markup=kb_subjects)
#
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Subjects')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📚 Subjects:</b>',
#                          reply_markup=kb_subjects)
#     # await message.answer(f'<b>📚 Subjects:</b>',
#     #                      reply_markup=kb_subjects)
#
#
# # ******************************************** CALCULUS
# @rate_limit(limit=3, key='📘 Calculus')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 Calculus')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📘 Calculus:</b>')
#     # path = '/root/bot/media/Calculus/1'
#     path = '/Users/pavelpopov/Downloads/Calculus'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         f.sort()
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#     # await message.answer(f'<b>📘 Calculus:</b>', reply_markup=kb_calculus3)
#
# @rate_limit(limit=3, key='Week 1: Properties of Elementary Functions')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 1: Properties of Elementary Functions')
# async def calculus_1(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 1:</b>\n\n')
#     # path = '/root/bot/media/Calculus/1'
#     path = '/Users/pavelpopov/Downloads/1'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         f.sort()
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 2: Infinite Sequences I')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 2: Infinite Sequences I')
# async def calculus_2(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 2:</b>\n\n')
#     path = '/root/bot/media/Calculus/2'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 3: Infinite Sequences II')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 3: Infinite Sequences II')
# async def calculus_3(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 3:</b>\n\n')
#     path = '/root/bot/media/Calculus/3'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 4: Limit of a function. Slant asymptotes')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 4: Limit of a function. Slant asymptotes')
# async def calculus_4(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 4:</b>\n\n')
#     path = '/root/bot/media/Calculus/4'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 5: Limit of a function. One-sided limits')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 5: Limit of a function. One-sided limits')
# async def calculus_5(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 5:</b>\n\n')
#     path = '/root/bot/media/Calculus/5'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 6: Discontinuous Functions and their Limits')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 6: Discontinuous Functions and their Limits')
# async def calculus_6(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 6:</b>\n\n')
#     path = '/root/bot/media/Calculus/6'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 7: Properties of Continuous Functions')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 7: Properties of Continuous Functions')
# async def calculus_7(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 7:</b>\n\n')
#     path = '/root/bot/media/Calculus/7'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 8: Review of Module I Topics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 8: Review of Module I Topics')
# async def calculus_8(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 8:</b>\n\n')
#     path = '/root/bot/media/Calculus/8'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 9: Her Majesty the Derivative. Differentiable functions, Derivatives of inverse and implicit functions')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 9: Her Majesty the Derivative. Differentiable functions, Derivatives of inverse and implicit functions')
# async def calculus_9(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 9:</b>\n\n')
#     path = '/root/bot/media/Calculus/9'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 10: Applications of derivative: rates of change, related rates')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 10: Applications of derivative: rates of change, related rates')
# async def calculus_10(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 10:</b>\n\n')
#     path = '/root/bot/media/Calculus/10'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 11: Applications of derivative: optimization')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 11: Applications of derivative: optimization')
# async def calculus_11(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 11:</b>\n\n')
#     path = '/root/bot/media/Calculus/11'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 12: The Mean Value Theorem. The second derivative test')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 12: The Mean Value Theorem. The second derivative test')
# async def calculus_12(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 12:</b>\n\n')
#     path = '/root/bot/media/Calculus/12'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 13: Functions concave up and concave down. Inflection points')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 13: Functions concave up and concave down. Inflection points')
# async def calculus_13(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 13:</b>\n\n')
#     path = '/root/bot/media/Calculus/13'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 14: Higher derivatives')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 14: Higher derivatives')
# async def calculus_14(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 14:</b>\n\n')
#     path = '/root/bot/media/Calculus/14'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 15: Taylor’s formula. Limits of complicated functions')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 15: Taylor’s formula. Limits of complicated functions')
# async def calculus_15(message: types.Message):
#     await message.answer(f'<b>📘 Calculus, week 15:</b>\n\n')
#     path = '/root/bot/media/Calculus/15'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📘 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 16')
# # async def calculus_16(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus, week 16:</b>\n\n')
# #     path = '/root/bot/media/Calculus/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📘 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 17')
# # async def calculus_17(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus, week 17:</b>\n\n')
# #     path = '/root/bot/media/Calculus/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📘 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 18')
# # async def calculus_18(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus, week 18:</b>\n\n')
# #     path = '/root/bot/media/Calculus/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📘 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 19')
# # async def calculus_19(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus, week 19:</b>\n\n')
# #     path = '/root/bot/media/Calculus/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📘 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 20')
# # async def calculus_20(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus, week 20:</b>\n\n')
# #     path = '/root/bot/media/Calculus/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📘 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 Books')
# async def command_professors(message: types.Message):
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Calculus/Books/Calculus - Jeffrey Lockshin.pdf')
#
#     await message.answer(f'<b>📘 Calculus books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/Calculus/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📘 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer(f'<b>📘 Calculus sources:</b>\n\n'
# #                          f'1️⃣ <ins><a href="https://www.khanacademy.org">khanacademy.org</a></ins>\n\n'
# #                          f'2️⃣ <ins><a href="https://www.wolframalpha.com">wolframalfa.com</a></ins>\n\n'
# #                          f'3️⃣ <ins><a href="https://www.desmos.com/calculator?lang=ru">desmos.com</a></ins>\n\n'
# #                          f'4️⃣ <ins><a href="http://andrewvorchik.com/for-students">andrewvorchik.com</a></ins>\n\n'
# #                          f'5️⃣ <ins><a href="http://mathprofi.ru">mathprofi.com</a></ins>'
# #                          )
#
# # @rate_limit(limit=3, key='📘 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📘 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📘 Calculus professors:</b>\n\n"
# #                          f"👤 <b>Патрик Анатолий Евгеньевич</b>\n"
# #                          f"Office hours: monday 16:10-17:20, G115 / tuesday 16:20-17:00 <a href='https://us05web.zoom.us/j/85614116394? pwd=a1lsYzNsWmtIZVZ4eXl0RmxsaTdnZz09'>ZOOM</a> (pass: Statistics), 17:10-17:50 <a href='https://us05web.zoom.us/j/83588807668? pwd=WnRmQlNMS1d4eFk2djVidUFhWlJEQT09'>ZOOM</a> (pass: Calculus)\n"
# #                          f"- apatrik@hse.ru\n\n"
# #                          f"👤 <b>Жуков Павел Владимирович</b>\n"
# #                          f"Office hours: wednesday (by appointment) 16:20-17:40, M202\n"
# #                          f"- pzhukov@hse.ru\n\n"
# #                          f"👤 <b>Ворчик Андрей Денисович</b>\n"
# #                          f"Office hours: monday (by appointment in VK) 16:20-17:20\n"
# #                          f"- avorchik@hse.ru\n\n"
# #                          f"👤 <b>Лукьянченко Пётр Павлович</b>\n"
# #                          f"- plukyanchenko@hse.ru\n\n"
# #                          f"👤 <b>Брыков Вячеслав Вячеславович</b>\n"
# #                          f"Office hours: friday (by appointment in Telegram) 16:20-17:20\n"
# #                          f"- vbrykov@hse.ru\n\n"
# #                          f"👤 <b>Шелике Аяна Георгиевна</b>\n"
# #                          f"- ashelike@hse.ru\n\n"
# #                          f"👤 <b>Хассан Яна Нибаль</b>\n"
# #                          f"Office hours: wednesday 16:20-17:20, M303\n"
# #                          f"- ykhassan@hse.ru"
# #                          )
#
#
# # ******************************************** STATISTICS
# @rate_limit(limit=3, key='📗 Statistics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 Statistics')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📗 Statistics:</b>')
#     # path = '/root/bot/media/Calculus/1'
#     path = '/Users/pavelpopov/Downloads/Statistics'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         f.sort()
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#     # await message.answer(f'<b>📗 Statistics:</b>', reply_markup=kb_statistics3)
#
# @rate_limit(limit=3, key='Week 1: Random events and their probabilities')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 1: Random events and their probabilities')
# async def Statistics_1(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 1:</b>\n\n')
#     path = '/root/bot/media/Statistics/1'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 2: Combinatorics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 2: Combinatorics')
# async def Statistics_2(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 2:</b>\n\n')
#     path = '/root/bot/media/Statistics/2'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 3: Conditional probability')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 3: Conditional probability')
# async def Statistics_3(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 3:</b>\n\n')
#     path = '/root/bot/media/Statistics/3'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 4: Independent random events')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 4: Independent random events')
# async def Statistics_4(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 4:</b>\n\n')
#     path = '/root/bot/media/Statistics/4'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 5: Random variables')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 5: Random variables')
# async def Statistics_5(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 5:</b>\n\n')
#     path = '/root/bot/media/Statistics/5'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 6: Expected value')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 6: Expected value')
# async def Statistics_6(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 6:</b>\n\n')
#     path = '/root/bot/media/Statistics/6'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 7: Variance')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 7: Variance')
# async def Statistics_7(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 7:</b>\n\n')
#     path = '/root/bot/media/Statistics/7'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 8: Independence and joint distributions')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 8: Independence and joint distributions')
# async def Statistics_8(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 8:</b>\n\n')
#     path = '/root/bot/media/Statistics/8'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 9: Functions of two random variables, covariance')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 9: Functions of two random variables, covariance')
# async def Statistics_9(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 9:</b>\n\n')
#     path = '/root/bot/media/Statistics/9'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 10: Continuous random variables')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 10: Continuous random variables')
# async def Statistics_10(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 10:</b>\n\n')
#     path = '/root/bot/media/Statistics/10'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 11: The normal distribution')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 11: The normal distribution')
# async def Statistics_11(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 11:</b>\n\n')
#     path = '/root/bot/media/Statistics/11'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 12: The normal distribution, part 2')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 12: The normal distribution, part 2')
# async def Statistics_12(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 12:</b>\n\n')
#     path = '/root/bot/media/Statistics/12'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 13: Limit theorems')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 13: Limit theorems')
# async def Statistics_13(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 13:</b>\n\n')
#     path = '/root/bot/media/Statistics/13'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 14: Revision excercises')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 14: Revision excercises')
# async def Statistics_14(message: types.Message):
#     await message.answer(f'<b>📗 Statistics, week 14:</b>\n\n')
#     path = '/root/bot/media/Statistics/14'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📗 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 15')
# # async def Statistics_15(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 15:</b>\n\n')
# #     path = '/root/bot/media/Statistics/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📗 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 16')
# # async def Statistics_16(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 16:</b>\n\n')
# #     path = '/root/bot/media/Statistics/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📗 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 17')
# # async def Statistics_17(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 17:</b>\n\n')
# #     path = '/root/bot/media/Statistics/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📗 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 18')
# # async def Statistics_18(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 18:</b>\n\n')
# #     path = '/root/bot/media/Statistics/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📗 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 19')
# # async def Statistics_19(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 19:</b>\n\n')
# #     path = '/root/bot/media/Statistics/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📗 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 20')
# # async def Statistics_20(message: types.Message):
# #     await message.answer(f'<b>📗 Statistics, week 20:</b>\n\n')
# #     path = '/root/bot/media/Statistics/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📗 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 Books')
# async def command_professors(message: types.Message):
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Statistics/Books/Durrett-Elementary_probability_for_applications.pdf')
#
#     await message.answer(f'<b>📗 Statistics books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/Statistics/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📗 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer('⚠️ Is not available yet.')
# #     # await message.answer(f'<b>📗 Microeconomics sources:</b>\n\n'
# #     #                      f'1️⃣ <ins><a href="https://academicearth.org/economics/#">academicearth.org</a></ins>\n\n'
# #     #                      f'2️⃣ <ins><a href="https://www.khanacademy.org/economics-finance-domain/microeconomics">khanacademy.org</a></ins>\n\n'
# #     #                      f'3️⃣ <ins><a href="https://www.edx.org/course/principles-of-microeconomics">edx.org</a></ins>'
# #     #                      )
#
# # @rate_limit(limit=3, key='📗 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📗 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📗 Statistics professors:</b>\n\n"
# #                          f"👤 <b>Патрик Анатолий Евгеньевич</b>\n"
# #                          f"Office hours: friday 13:00-14:20, D203 / tuesday 16:20-17:00 <a href='https://us05web.zoom.us/j/85614116394? pwd=a1lsYzNsWmtIZVZ4eXl0RmxsaTdnZz09'>ZOOM</a> (pass: Statistics), 17:10-17:50 <a href='https://us05web.zoom.us/j/83588807668? pwd=WnRmQlNMS1d4eFk2djVidUFhWlJEQT09'>ZOOM</a> (pass: Calculus)\n"
# #                          f"- apatrik@hse.ru\n\n"
# #                          f"👤 <b>Люлько Ярослав Александрович</b>\n"
# #                          f"Office hours: friday 18:30-19:30, R506\n"
# #                          f"- ylyulko@hse.ru\n\n"
# #                          f"👤 <b>Шелике Аяна Георгиевна</b>\n"
# #                          f"- ashelike@hse.ru\n\n"
# #                          f"👤 <b>Житлухин Михаил Валентинович</b>\n"
# #                          f"Office hours: monday 16:20-17:40, R208\n"
# #                          f"- mzhitlukhin@hse.ru\n\n"
# #                          f"👤 <b>Потапов Денис Игоревич</b>\n"
# #                          f"Office hours: saturday 11:00-12:30, D103\n"
# #                          f"- dipotapov@hse.ru"
# #                          )
#
#
#
#
# # ******************************************** MICROECONOMICS
# @rate_limit(limit=3, key='📙 Microeconomics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Microeconomics')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics:</b>')
#     # path = '/root/bot/media/Calculus/1'
#     path = '/Users/pavelpopov/Downloads/Microeconomics'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         f.sort()
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#     # await message.answer(f'<b>📙 Microeconomics:</b>', reply_markup=kb_microeconomics3)
#
# # @rate_limit(limit=3, key='📙 Classes')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Classes')
# # async def command_professors(message: types.Message):
# #     chat_id = message.from_user.id
# #     # pdf_bytes1 = InputFile(path_or_bytesio='media/Microeconomics/Classes/Lecture2_2022.pdf')
# #
# #     await message.answer(f'<b>📙 Microeconomics classes:</b>\n\n')
# #     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes1, caption='<b>🕓 13.09</b>')
# #     path = '/root/bot/media/Microeconomics/Classes'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 Homework')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Homework')
# # async def command_professors(message: types.Message):
# #     # await message.answer('⚠️ Is not available yet.')
# #     chat_id = message.from_user.id
# #
# #     # pdf_bytes1 = InputFile(path_or_bytesio='media/Microeconomics/Homework/HW2_2022.pdf')
# #
# #     await message.answer(f'<b>📙 Microeconomics homework:</b>\n\n')
# #     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes2, caption='<b>🕓 13.09</b>')
# #     path = '/root/bot/media/Microeconomics/Homework'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 1: Introduction to Economics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 1: Introduction to Economics')
# async def Microeconomics_1(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 1:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/1'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 2: Comparative Advantage and Exchange Comparative advantage')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 2: Comparative Advantage and Exchange Comparative advantage')
# async def Microeconomics_2(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 2:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/2'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 3: Supply and Demand')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 3: Supply and Demand')
# async def Microeconomics_3(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 3:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/3'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 4: Elasticity')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 4: Elasticity')
# async def Microeconomics_4(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 4:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/4'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 5: Consumer Choice')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 5: Consumer Choice')
# async def Microeconomics_5(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 5:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/5'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 6: Producer Theory: Revenues and Costs')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 6: Producer Theory: Revenues and Costs')
# async def Microeconomics_6(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 6:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/6'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 7: Short-Run and Long-Run. Perfect competition')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 7: Short-Run and Long-Run. Perfect competition')
# async def Microeconomics_7(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 7:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/7'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 8: Monopoly and Monopolistic Competition')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 8: Monopoly and Monopolistic Competition')
# async def Microeconomics_8(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 8:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/8'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 9: Oligopoly')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 9: Oligopoly')
# async def Microeconomics_9(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 9:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/9'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 10: Factor Markets: Labor Market')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 10: Factor Markets: Labor Market')
# async def Microeconomics_10(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 10:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/10'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 11: Market Failures. Externalities and Public Goods')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 11: Market Failures. Externalities and Public Goods')
# async def Microeconomics_11(message: types.Message):
#     await message.answer(f'<b>📙 Microeconomics, week 11:</b>\n\n')
#     path = '/root/bot/media/Microeconomics/11'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📙 12')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 12')
# # async def Microeconomics_12(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 12:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/12'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 13')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 13')
# # async def Microeconomics_13(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 13:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/13'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 14')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 14')
# # async def Microeconomics_14(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 14:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/14'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 15')
# # async def Microeconomics_15(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 15:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 16')
# # async def Microeconomics_16(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 16:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 17')
# # async def Microeconomics_17(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 17:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 18')
# # async def Microeconomics_18(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 18:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 19')
# # async def Microeconomics_19(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 19:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📙 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 20')
# # async def Microeconomics_20(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics, week 20:</b>\n\n')
# #     path = '/root/bot/media/Microeconomics/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📙 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Books')
# async def command_professors(message: types.Message):
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Microeconomics/Books/CFO_chapter1.pdf')
#
#     await message.answer(f'<b>📙 Microeconomics books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/Microeconomics/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📙 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer(f'<b>📙 Microeconomics sources:</b>\n\n'
# #                          f'1️⃣ <ins><a href="https://academicearth.org/economics/#">academicearth.org</a></ins>\n\n'
# #                          f'2️⃣ <ins><a href="https://www.khanacademy.org/economics-finance-domain/microeconomics">khanacademy.org</a></ins>\n\n'
# #                          f'3️⃣ <ins><a href="https://www.edx.org/course/principles-of-microeconomics">edx.org</a></ins>'
# #                          )
#
# # @rate_limit(limit=3, key='📙 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📙 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📙 Microeconomics professors:</b>\n\n"
# #                          f"👤 <b>Юрко Анна Вячеславовна\n</b>"
# #                          f"Office hours: tuesday 16:20-17:20, S735\n"
# #                          f"- ayurko@hse.ru\n\n"
# #                          f"👤 <b>Ворчик Андрей Денисович</b>\n"
# #                          f"- avorchik@hse.ru\n\n"
# #                          f"👤 <b>Автономов Юрий Владимирович</b>\n"
# #                          f"Office hours: monday 13:00-14:00, S1002\n"
# #                          f"- yavtonomov@hse.ru\n\n"
# #                          f"👤 <b>Верем Ирина Юрьевна</b>\n"
# #                          f"Office hours: friday 14:40-16:00, R201\n"
# #                          f"- iverem@hse.ru\n\n"
# #                          f"👤 <b>Векилян Армине Вегенаковна</b>\n"
# #                          f"- avekilyan@hse.ru\n\n"
# #                          f"👤 <b>Чернышова Яна Алексеевна</b>\n"
# #                          f"- ychernyshova@hse.ru\n\n"
# #                          f"👤 <b>Зимрутян Гаянэ Аршаковна</b>\n"
# #                          f"Office hours: monday (by appointment)\n"
# #                          f"- gzimrutyan@hse.ru"
# #                          )
#
#
#
# # ******************************************** MACROECONOMICS
# @rate_limit(limit=3, key='📕 Macroeconomics')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 Macroeconomics')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📕 Macroeconomics:</b>',
#                          reply_markup=kb_macroeconomics3)
#
# # @rate_limit(limit=3, key='📕 1')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 1')
# # async def Macroeconomics_1(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 1:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/1'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 2')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 2')
# # async def Macroeconomics_2(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 2:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/2'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 3')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 3')
# # async def Macroeconomics_3(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 3:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/3'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 4')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 4')
# # async def Macroeconomics_4(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 4:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/4'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 5')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 5')
# # async def Macroeconomics_5(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 5:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/5'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 6')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 6')
# # async def Macroeconomics_6(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 6:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/6'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 7')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 7')
# # async def Macroeconomics_7(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 7:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/7'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 8')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 8')
# # async def Macroeconomics_8(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 8:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/8'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 9')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 9')
# # async def Macroeconomics_9(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 9:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/9'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 10')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 10')
# # async def Macroeconomics_10(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 10:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/10'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 11')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 11')
# # async def Macroeconomics_11(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 11:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/11'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 12')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 12')
# # async def Macroeconomics_12(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 12:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/12'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 13')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 13')
# # async def Macroeconomics_13(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 13:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/13'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 14')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 14')
# # async def Macroeconomics_14(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 14:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/14'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 15')
# # async def Macroeconomics_15(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 15:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 16')
# # async def Macroeconomics_16(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 16:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 17')
# # async def Macroeconomics_17(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 17:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 18')
# # async def Macroeconomics_18(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 18:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 19')
# # async def Macroeconomics_19(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week 19:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📕 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 20')
# # async def Macroeconomics_20(message: types.Message):
# #     await message.answer(f'<b>📕 Macroeconomics, week:</b>\n\n')
# #     path = '/root/bot/media/Macroeconomics/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📕 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 Books')
# async def command_professors(message: types.Message):
#     await message.answer('⚠️ Is not available yet.')
#     # chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Microeconomics/Books/CFO_chapter1.pdf')
#     #
#     # await message.answer(f'<b>📕 Microeconomics books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     # path = '/root/bot/media/Macroeconomics/Books'
#     # files = []
#     # # r = root, d = directories, f = files
#     # for r, d, f in os.walk(path):
#     #     for file in f:
#     #         files.append(os.path.join(r, file))
#     # for f in files:
#     #     await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     # await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📕 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer('⚠️ Is not available yet.')
# #     # await message.answer(f'<b>📕 Microeconomics sources:</b>\n\n'
# #     #                      f'1️⃣ <ins><a href="https://academicearth.org/economics/#">academicearth.org</a></ins>\n\n'
# #     #                      f'2️⃣ <ins><a href="https://www.khanacademy.org/economics-finance-domain/microeconomics">khanacademy.org</a></ins>\n\n'
# #     #                      f'3️⃣ <ins><a href="https://www.edx.org/course/principles-of-microeconomics">edx.org</a></ins>'
# #     #                      )
#
# # @rate_limit(limit=3, key='📕 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📕 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer('⚠️ Is not available yet.')
#
#
#
# # ******************************************** HISTORY
# @rate_limit(limit=3, key='📔 History')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 History')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📔 History:</b>')
#     # path = '/root/bot/media/Calculus/1'
#     path = '/Users/pavelpopov/Downloads/History'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         f.sort()
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#     # await message.answer(f'<b>📔 History:</b>', reply_markup=kb_history3)
#
# @rate_limit(limit=3, key='Week 1: Introduction. The Axial Age')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 1: Introduction. The Axial Age')
# async def History_1(message: types.Message):
#     await message.answer(f'<b>📔 History, week 1:</b>\n\n')
#     path = '/root/bot/media/History/1'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 2: Ancient India: Vedanta, Buddhism')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 2: Ancient India: Vedanta, Buddhism')
# async def History_2(message: types.Message):
#     await message.answer(f'<b>📔 History, week 2:</b>\n\n')
#     path = '/root/bot/media/History/2'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 3: Ancient China: Confucianism, Daosism, Legalism')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 3: Ancient China: Confucianism, Daosism, Legalism')
# async def History_3(message: types.Message):
#     await message.answer(f'<b>📔 History, week 3:</b>\n\n')
#     path = '/root/bot/media/History/3'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 4: Ancient Israel: the rise of monotheism')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 4: Ancient Israel: the rise of monotheism')
# async def History_4(message: types.Message):
#     await message.answer(f'<b>📔 History, week 4:</b>\n\n')
#     path = '/root/bot/media/History/4'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📔 5')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 5')
# # async def History_5(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 5:</b>\n\n')
# #     path = '/root/bot/media/History/5'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 6')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 6')
# # async def History_6(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 6:</b>\n\n')
# #     path = '/root/bot/media/History/6'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 7')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 7')
# # async def History_7(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 7:</b>\n\n')
# #     path = '/root/bot/media/History/7'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 8')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 8')
# # async def History_8(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 8:</b>\n\n')
# #     path = '/root/bot/media/History/8'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 9')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 9')
# # async def History_9(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 9:</b>\n\n')
# #     path = '/root/bot/media/History/9'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 10')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 10')
# # async def History_10(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 10:</b>\n\n')
# #     path = '/root/bot/media/History/10'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 11')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 11')
# # async def History_11(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 11:</b>\n\n')
# #     path = '/root/bot/media/History/11'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 12')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 12')
# # async def History_12(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 12:</b>\n\n')
# #     path = '/root/bot/media/History/12'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 13')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 13')
# # async def History_13(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 13:</b>\n\n')
# #     path = '/root/bot/media/History/13'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 14')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 14')
# # async def History_14(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 14:</b>\n\n')
# #     path = '/root/bot/media/History/14'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 15')
# # async def History_15(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 15:</b>\n\n')
# #     path = '/root/bot/media/History/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 16')
# # async def History_16(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 16:</b>\n\n')
# #     path = '/root/bot/media/History/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 17')
# # async def History_17(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 17:</b>\n\n')
# #     path = '/root/bot/media/History/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 18')
# # async def History_18(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 18:</b>\n\n')
# #     path = '/root/bot/media/History/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 19')
# # async def History_19(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 19:</b>\n\n')
# #     path = '/root/bot/media/History/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📔 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 20')
# # async def History_20(message: types.Message):
# #     await message.answer(f'<b>📔 History, week 20:</b>\n\n')
# #     path = '/root/bot/media/History/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📔 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 Books')
# async def command_professors(message: types.Message):
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/History/Books/History - Jeffrey Lockshin.pdf')
#
#     await message.answer(f'<b>📔 History books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/History/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📔 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer(f'⚠️ Is not avaliable yet.'
# #                          # f'<b>📔 History sources:</b>\n\n'
# #                          # f'1️⃣ <ins><a href="https://www.khanacademy.org">khanacademy.org</a></ins>\n\n'
# #                          # f'2️⃣ <ins><a href="https://www.wolframalpha.com">wolframalfa.com</a></ins>\n\n'
# #                          # f'3️⃣ <ins><a href="https://www.desmos.com/calculator?lang=ru">desmos.com</a></ins>\n\n'
# #                          # f'4️⃣ <ins><a href="http://andrewvorchik.com/for-students">andrewvorchik.com</a></ins>\n\n'
# #                          # f'5️⃣ <ins><a href="http://mathprofi.ru">mathprofi.com</a></ins>'
# #                          )
#
# # @rate_limit(limit=3, key='📔 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📔 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📔 History professors:</b>\n\n"
# #                          # f"⚠️ Is not avaliable yet."
# #                          f"👤 <b>Царева Александра Петровна</b>\n"
# #                          f"Office hours: monday (by appointment) 16:30-17:40, <a href='https://us04web.zoom.us/j/75523474837'>ZOOM</a> (pass: ICEF)\n"
# #                          f"- atsareva@hse.ru\n\n"
# #                          f"👤 <b>Отдельнов Марк Михайлович</b>\n"
# #                          f"- motdelnov@hse.ru\n\n"
# #                          f"👤 <b>Петрова Мария Святославовна</b>\n"
# #                          f"- mspetrova@hse.ru\n\n"
# #                          )
#
#
#
# # ******************************************** PHILOSOPHY
# @rate_limit(limit=3, key='📒 Philosophy')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 Philosophy')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📒 Philosophy:</b>',
#                          reply_markup=kb_philosophy3)
#
# # @rate_limit(limit=3, key='📒 1')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 1')
# # async def Philosophy_1(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 1:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/1'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 2')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 2')
# # async def Philosophy_2(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 2:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/2'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 3')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 3')
# # async def Philosophy_3(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 3:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/3'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 4')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 4')
# # async def Philosophy_4(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 4:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/4'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 5')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 5')
# # async def Philosophy_5(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 5:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/5'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 6')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 6')
# # async def Philosophy_6(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 6:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/6'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 7')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 7')
# # async def Philosophy_7(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 7:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/7'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 8')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 8')
# # async def Philosophy_8(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 8:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/8'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 9')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 9')
# # async def Philosophy_9(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 9:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/9'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 10')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 10')
# # async def Philosophy_10(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 10:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/10'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 11')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 11')
# # async def Philosophy_11(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 11:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/11'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 12')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 12')
# # async def Philosophy_12(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 12:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/12'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 13')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 13')
# # async def Philosophy_13(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 13:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/13'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 14')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 14')
# # async def Philosophy_14(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 14:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/14'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 15')
# # async def Philosophy_15(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 15:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 16')
# # async def Philosophy_16(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 16:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 17')
# # async def Philosophy_17(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 17:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 18')
# # async def Philosophy_18(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 18:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 19')
# # async def Philosophy_19(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 19:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📒 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 20')
# # async def Philosophy_20(message: types.Message):
# #     await message.answer(f'<b>📒 Philosophy, week 20:</b>\n\n')
# #     path = '/root/bot/media/Philosophy/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📒 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 Books')
# async def command_professors(message: types.Message):
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Philosophy/Books/Philosophy - Jeffrey Lockshin.pdf')
#
#     await message.answer(f'<b>📒 Philosophy books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/Philosophy/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📒 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer(f'⚠️ Is not avaliable yet.'
# #                          # f'<b>📒 Philosophy sources:</b>\n\n'
# #                          # f'1️⃣ <ins><a href="https://www.khanacademy.org">khanacademy.org</a></ins>\n\n'
# #                          # f'2️⃣ <ins><a href="https://www.wolframalpha.com">wolframalfa.com</a></ins>\n\n'
# #                          # f'3️⃣ <ins><a href="https://www.desmos.com/calculator?lang=ru">desmos.com</a></ins>\n\n'
# #                          # f'4️⃣ <ins><a href="http://andrewvorchik.com/for-students">andrewvorchik.com</a></ins>\n\n'
# #                          # f'5️⃣ <ins><a href="http://mathprofi.ru">mathprofi.com</a></ins>'
# #                          )
#
# # @rate_limit(limit=3, key='📒 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📒 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📒 Philosophy professors:</b>\n\n"
# #                          # f"⚠️ Is not avaliable yet."
# #                          f"👤 <b>Сейрсингх Кристер Раджендра</b>\n"
# #                          f"- sairsingh@hse.ru\n\n"
# #                          f"👤 <b>Отдельнов Марк Михайлович</b>\n"
# #                          f"- motdelnov@hse.ru\n\n"
# #                          )
#
#
#
# # ******************************************** ENGLISH
# # @rate_limit(limit=3, key='🇬🇧 English')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 English')
# # async def command_professors(message: types.Message):
# #     await message.answer(f'<b>🇬🇧 English:</b>',
# #                          reply_markup=kb_english2)
# #
# # @rate_limit(limit=3, key='🇬🇧 Classes')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 Classes')
# # async def command_professors(message: types.Message):
# #     # await message.answer('⚠️ Is not available yet.')
# #     chat_id = message.from_user.id
# #     # pdf_bytes = InputFile(path_or_bytesio='media/English/Classes/Economic terms.pdf')
# #
# #     await message.answer(f'<b>🇬🇧 English classes:</b>\n\n')
# #     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes, caption='<b>🕓 04.09</b>')
# #     path = '/root/bot/media/English/Classes'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='🇬🇧 Homework')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 Homework')
# # async def command_professors(message: types.Message):
# #     chat_id = message.from_user.id
# #
# #     # await message.answer('⚠️ Is not available yet.')
# #
# #     await message.answer(f'<b>🇬🇧 English homework:</b>\n\n')
# #     path = '/root/bot/media/English/Homework'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='🇬🇧 Books')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 Books')
# # async def command_professors(message: types.Message):
# #     # await message.answer('⚠️ Is not available yet.')
# #     chat_id = message.from_user.id
# #     # pdf_bytes = InputFile(path_or_bytesio='media/English/Books/Economics Christopher St J Yates.pdf')
# #
# #     await message.answer(f'<b>🇬🇧 English books:</b>\n\n')
# #     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
# #     path = '/root/bot/media/English/Books'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='🇬🇧 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer('⚠️ Is not available yet.')
# #     # await message.answer(f'<b>🇬🇧 Microeconomics sources:</b>\n\n'
# #     #                      f'1️⃣ <ins><a href="https://academicearth.org/economics/#">academicearth.org</a></ins>\n\n'
# #     #                      f'2️⃣ <ins><a href="https://www.khanacademy.org/economics-finance-domain/microeconomics">khanacademy.org</a></ins>\n\n'
# #     #                      f'3️⃣ <ins><a href="https://www.edx.org/course/principles-of-microeconomics">edx.org</a></ins>'
# #     #                      )
# #
# # @rate_limit(limit=3, key='🇬🇧 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🇬🇧 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>🇬🇧 English professors:</b>\n\n"
# #                          f"👤 <b>Балакирева Марина Алексеевна\n</b>"
# #                          f"- mbalakireva@hse.ru\n\n"
# #                          f"👤 <b>Джек Ризотти</b>\n"
# #                          f"- rjack@hse.ru\n\n"
# #                          f"👤 <b>Милберн Бродей Еван</b>\n"
# #                          f"- bemilburn@hse.ru\n\n"
# #                          f"👤 <b>Даннет Марк Джонсон</b>\n"
# #                          f"- mj.dunnett@hse.ru\n\n"
# #                          f"👤 <b>Колядина Наталия Борисовна</b>\n"
# #                          f"Office hours: thursday (by appointment) 17:00-18:00, <a href='https://us02web.zoom.us/meeting/83066642482'>ZOOM</a>\n"
# #                          f"- nkoliadina@hse.ru\n\n"
# #                          f"👤 <b>Манн Манджит Сингх</b>\n"
# #                          f"- msmann@hse.ru"
# #                          )
#
#
#
# # ******************************************** INFO
# @rate_limit(limit=3, key='📓 ICS')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 ICS')
# async def command_professors(message: types.Message):
#     await message.answer(f'<b>📓 ICS:</b>',
#                          reply_markup=kb_ics3)
#
# @rate_limit(limit=3, key='Week 1: Using built-in functions for data analysis')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 1: Using built-in functions for data analysis')
# async def ICS_1(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 1:</b>\n\n')
#     path = '/root/bot/media/ICS/1'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 2: Graphical Data Analysis in MS Excel')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 2: Graphical Data Analysis in MS Excel')
# async def ICS_2(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 2:</b>\n\n')
#     path = '/root/bot/media/ICS/2'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 3: MS Excel Add-ins for solving economic tasks')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 3: MS Excel Add-ins for solving economic tasks')
# async def ICS_3(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 3:</b>\n\n')
#     path = '/root/bot/media/ICS/3'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 4: Using Formulas and formatting for Conditional Analysis')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 4: Using Formulas and formatting for Conditional Analysis')
# async def ICS_4(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 4:</b>\n\n')
#     path = '/root/bot/media/ICS/4'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 5: Working with large series of data')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 5: Working with large series of data')
# async def ICS_5(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 5:</b>\n\n')
#     path = '/root/bot/media/ICS/5'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 6: Introduction to Macros and VBA. Introduction to Macros and VBA. Recording macros')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 6: Introduction to Macros and VBA. Introduction to Macros and VBA. Recording macros')
# async def ICS_6(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 6:</b>\n\n')
#     path = '/root/bot/media/ICS/6'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 7: MS Excel objects')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 7: MS Excel objects')
# async def ICS_7(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 7:</b>\n\n')
#     path = '/root/bot/media/ICS/7'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 8: Variables and data types. Manipulating data')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 8: Variables and data types. Manipulating data')
# async def ICS_8(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 8:</b>\n\n')
#     path = '/root/bot/media/ICS/8'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 9: Loop and Conditional Statements used in VBA Excel programming')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 9: Loop and Conditional Statements used in VBA Excel programming')
# async def ICS_9(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 9:</b>\n\n')
#     path = '/root/bot/media/ICS/9'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='Week 10: User Forms')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Week 10: User Forms')
# async def ICS_10(message: types.Message):
#     await message.answer(f'<b>📓 ICS, week 10:</b>\n\n')
#     path = '/root/bot/media/ICS/10'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📓 11')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 11')
# # async def ICS_11(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 11:</b>\n\n')
# #     path = '/root/bot/media/ICS/11'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 12')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 12')
# # async def ICS_12(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 12:</b>\n\n')
# #     path = '/root/bot/media/ICS/12'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 13')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 13')
# # async def ICS_13(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 13:</b>\n\n')
# #     path = '/root/bot/media/ICS/13'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 14')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 14')
# # async def ICS_14(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 14:</b>\n\n')
# #     path = '/root/bot/media/ICS/14'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 15')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 15')
# # async def ICS_15(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 15:</b>\n\n')
# #     path = '/root/bot/media/ICS/15'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 16')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 16')
# # async def ICS_16(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 16:</b>\n\n')
# #     path = '/root/bot/media/ICS/16'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 17')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 17')
# # async def ICS_17(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 17:</b>\n\n')
# #     path = '/root/bot/media/ICS/17'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 18')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 18')
# # async def ICS_18(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 18:</b>\n\n')
# #     path = '/root/bot/media/ICS/18'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 19')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 19')
# # async def ICS_19(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 19:</b>\n\n')
# #     path = '/root/bot/media/ICS/19'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
# #
# # @rate_limit(limit=3, key='📓 20')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 20')
# # async def ICS_20(message: types.Message):
# #     await message.answer(f'<b>📓 ICS, week 20:</b>\n\n')
# #     path = '/root/bot/media/ICS/20'
# #     files = []
# #     # r = root, d = directories, f = files
# #     for r, d, f in os.walk(path):
# #         for file in f:
# #             files.append(os.path.join(r, file))
# #     for f in files:
# #         await dp.bot.send_document(chat_id=message.from_user.id, document=open(f, 'rb'))
# #     await message.answer("<b>That's it for now.</b>")
#
# @rate_limit(limit=3, key='📓 Books')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 Books')
# async def command_professors(message: types.Message):
#     # await message.answer('⚠️ Is not available yet.')
#     chat_id = message.from_user.id
#     # pdf_bytes = InputFile(path_or_bytesio='media/Microeconomics/Books/CFO_chapter1.pdf')
#
#     await message.answer(f'<b>📓 ICS books:</b>\n\n')
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes)
#     path = '/root/bot/media/ICS/Books'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#     await message.answer("<b>That's it for now.</b>")
#
# # @rate_limit(limit=3, key='📓 Sources')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 Sources')
# # async def command_professors(message: types.Message):
# #     await message.answer('⚠️ Is not available yet.')
# #     # await message.answer(f'<b>📓 Microeconomics sources:</b>\n\n'
# #     #                      f'1️⃣ <ins><a href="https://academicearth.org/economics/#">academicearth.org</a></ins>\n\n'
# #     #                      f'2️⃣ <ins><a href="https://www.khanacademy.org/economics-finance-domain/microeconomics">khanacademy.org</a></ins>\n\n'
# #     #                      f'3️⃣ <ins><a href="https://www.edx.org/course/principles-of-microeconomics">edx.org</a></ins>'
# #     #                      )
#
# # @rate_limit(limit=3, key='📓 Professors')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📓 Professors')
# # async def command_professors(message: types.Message):
# #     await message.answer(f"<b>📓 ICS professors:</b>\n\n"
# #                          f"👤 <b>Акиншин Анатолий Анатольевич</b>\n"
# #                          f"Office hours: thursday 18:00-19:30, R603\n"
# #                          f"- aakinshin@hse.ru\n\n"
# #                          f"👤 <b>Бессонова Ирина Анатольевна</b>\n"
# #                          f"Office hours: tuesday/friday 18:00-20:00, R608/R614\n"
# #                          f"- ibes@hse.ru"
# #                          )
#
#
#
#
#
#
#
