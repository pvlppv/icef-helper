# import random
# import time
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton
# from pyqiwip2p.p2p_types import custom_fields, custom_fields
# from pyrogram.raw.base import account_days_ttl
# from handlers.users.markups import buy_menu
#
# from data.config import admins
# from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, IsSubscriberChannelMessage
# from keyboards.inline import ikb_subscription, ikb_subscription2
# from loader import dp, bot, db_sql
# from states import editsub
# from utils.db_api import quick_commands
# from utils.misc import rate_limit
# from pyqiwip2p import QiwiP2P
#
# import time
# import datetime
#
# YOOTOKEN = '381764678:TEST:42212'
# QIWI_TOKEN = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Im9mOThmcS0wMCIsInVzZXJfaWQiOiI3OTI5NTQ5MzI0MCIsInNlY3JldCI6IjYyM2Q2ODJjOTAxNDJmMDZhY2QxMzE1ZDcxMDIwODY0NjE1MWFiODU2ZWQwNDZmNTlhMWNkNDE2NmYxOTI2MjAifX0='
# p2p = QiwiP2P(auth_key=QIWI_TOKEN)
#
# def days_to_seconds(days):
#     return days * 24 * 60 * 60
#
# def minutes_to_seconds(minutes):
#     return minutes * 60
#
# def time_sub_day(get_time):
#     time_now = int(time.time())
#     middle_time = int(get_time) - time_now
#
#     if middle_time <= 0:
#         return False
#     else:
#         dt = str(datetime.timedelta(seconds=middle_time))
#         return dt
#
#
# @rate_limit(limit=3, key='/subscription')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='/subscription')
# async def command_subscription(message: types.Message):
#     await message.answer(f'<b>⭐️ Subscription to ICEF Helper:</b>\n\n'
#                                   f'<b>Features:</b>\n'
#                                   # f'🔒 Приватный доступ\n'
#                                   # f'⭐️ Система платной подписки\n'
#                                   f'👤 Profile - личный/чужой профиль с автоматически обновляющимся рейтингом\n'
#                                   f'🗃 Handbook - быстрый доступ к справочнику студента\n'
#                                   f'📂 Materials - полезные материалы по учёбе и работе\n'
#                                   f'🗣 Chats - беседы по интересам\n'
#                                   f'📚 Subjects - предметы с актуальной информацией по ним (classes, homeworks, books, sources, professors, office hours)\n'
#                                   f'🔔 Timetable - расписание пар у всех групп\n'
#                                   f'🚪 Locations - расположение важных мест на Покровке\n'
#                                   f'🗞 ICEF news - новости с icef.hse.ru с автоматической рассылкой\n'
#                                   f'🎫 ICEF events - ближайшие ICEF события\n'
#                                   f"⚙️ Settings - настройки (изменение профиля, репорт etc.)\n"
#                                   # f"⚠️ Анти-спам система\n"
#                                   f'🔊 Рассылка напоминалок, объявлений и прочего\n'
#                                   f"💠 Платформа Smart LMS прямо из диалога с ботом\n\n"
#                                   f'<b>Price:</b> 49 rub/month'
#                          ,
#                          reply_markup=ikb_subscription)
#
# # @rate_limit(limit=3, key='⭐️ Subscription')
# # @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⭐️ Subscription')
# # async def command_subscription(message: types.Message):
# #     await message.answer(f'<b>⭐️ Subscription to ICEF Helper:</b>\n\n'
# #                                   f'<b>Features:</b>\n'
# #                                   # f'🔒 Приватный доступ\n'
# #                                   # f'⭐️ Система платной подписки\n'
# #                                   f'👤 Profile - личный/чужой профиль с автоматически обновляющимся рейтингом\n'
# #                                   f'🗃 Handbook - быстрый доступ к справочнику студента\n'
# #                                   f'📂 Materials - полезные материалы по учёбе и работе\n'
# #                                   f'🗣 Chats - беседы по интересам\n'
# #                                   f'📚 Subjects - предметы с актуальной информацией по ним (classes, homeworks, books, sources, professors, office hours)\n'
# #                                   f'🔔 Timetable - расписание пар у всех групп\n'
# #                                   f'🚪 Locations - расположение важных мест на Покровке\n'
# #                                   f'🗞 ICEF news - новости с icef.hse.ru с автоматической рассылкой\n'
# #                                   f'🎫 ICEF events - ближайшие ICEF события\n'
# #                                   f"⚙️ Settings - настройки (изменение профиля, репорт etc.)\n"
# #                                   # f"⚠️ Анти-спам система\n"
# #                                   f'🔊 Рассылка напоминалок, объявлений и прочего\n'
# #                                   f"💠 Платформа Smart LMS прямо из диалога с ботом\n\n"
# #                                   f'<b>Price:</b> 49 rub/month'
# #                          ,
# #                          reply_markup=ikb_subscription)
#
# @dp.callback_query_handler(text='purchase')
# async def subscription_month(call: types.CallbackQuery):
#     username = call.from_user.username
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     comment = f'Month subscription to Telegram Bot «ICEF Helper». Telegram Username: @{username}. Bill ID: ' + str(random.randint(1000, 9999))
#     themecode = 'Pavel-Pwuw3_kOrl'
#     bill = p2p.bill(amount=49, lifetime=15, comment=comment, theme_code=themecode)
#     # bill_firstsubscribers = p2p.bill(amount=49, lifetime=15, comment=comment, theme_code=themecode)
#     db_sql.add_check(call.from_user.id, bill.bill_id)
#     await call.message.answer(f'<b>🧾 Your payment bill is ready.</b>\n\n'
#                               f'❗️ After the payment click the button "Check payment status" and you will automatically get a full access to the bot.',
#                          reply_markup=buy_menu(url=bill.pay_url, bill=bill.bill_id))
#
# @dp.callback_query_handler(text_contains='check_')
# async def check(call: types.CallbackQuery):
#     bill = str(call.data[6:])
#     info = db_sql.get_check(bill)
#     if info != False:
#         if str(p2p.check(bill_id=bill).status) == 'PAID':
#             if db_sql.user_exists(call.from_user.id):
#                 sub_time = int(time.time()) + days_to_seconds(30)
#                 db_sql.set_sub_time(call.from_user.id, sub_time)
#                 await bot.send_message(call.from_user.id,
#                                         '<b>⭐️ You successfully purchased a month subscription to ICEF Helper. Now you have a full access to the bot.</b>\n\n'
#                                         'To see its expiration date, check your profile.')
#                 db_sql.delete_check(call.from_user.id)
#             else:
#                 db_sql.add_user(call.from_user.id)
#                 sub_time = int(time.time()) + days_to_seconds(30)
#                 db_sql.set_sub_time(call.from_user.id, sub_time)
#                 await bot.send_message(call.from_user.id,
#                                         '<b>⭐️ You successfully purchased a month subscription to ICEF Helper. Now you have a full access to the bot.</b>\n\n'
#                                         'To see its expiration date, check your profile.')
#                 db_sql.delete_check(call.from_user.id)
#         else:
#             await call.answer("⚠️ Not payed yet.", show_alert=True)
#     else:
#         await call.answer('⚠️ Your payment bill is not found. Contact with @paoloppv.', show_alert=True)
#
#
#
#
# #     await bot.send_invoice(chat_id=call.from_user.id,
# #                            title='Subscription for ICEF Helper',
# #                            description='Month subscription for telegram bot «ICEF Helper».',
# #                            payload='sub_month',
# #                            provider_token=YOOTOKEN,
# #                            currency='RUB',
# #                            start_parameter='ICEF_Helper',
# #                            prices=[{'label': 'Руб', 'amount': 4900}])
# #
# # @dp.callback_query_handler(text='cancel')
# # async def cancel(call: types.CallbackQuery):
# #     await call.message.edit_text(f'<b>❌ Purchasing of the subscription is canceled.</b>')
# #
# # @dp.pre_checkout_query_handler()
# # async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
# #     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
# #
# # @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# # async def pay(message: types.Message):
# #     if message.successful_payment.invoice_payload == 'sub_month':
# #         if db_sql.user_exists(message.from_user.id):
# #             sub_time = int(time.time()) + days_to_seconds(1)
# #             db_sql.set_sub_time(message.from_user.id, sub_time)
# #             await bot.send_message(message.from_user.id,
# #                                    '✅ You successfully purchased a month subscription for «ICEF Helper». Now you have a full access to the bot.\n\n'
# #                                    'Too see its expiration date, check your profile.')
# #         else:
# #             db_sql.add_user(message.from_user.id)
# #             sub_time = int(time.time()) + days_to_seconds(1)
# #             db_sql.set_sub_time(message.from_user.id, sub_time)
# #             await bot.send_message(message.from_user.id,
# #                                    '✅ You successfully purchased a month subscription for «ICEF Helper». Now you have a full access to the bot.\n\n'
# #                                    'Too see its expiration date, check your profile.')
#
# # @dp.message_handler(IsPrivateMessage(), text='/editsubforeveryone', chat_id=admins)
# # async def edit_sub(message: types.Message):
# #     users = await quick_commands.select_all_users()
# #     for user in users:
# #         try:
# #             sub_time = int(time.time()) + days_to_seconds(30)
# #             db_sql.set_sub_time(user.user_id, sub_time)
# #         except Exception:
# #             pass
# #     await message.answer('1 month subscription was given to everybody.')
#
# @dp.message_handler(IsPrivateMessage(), text='/editsub', chat_id=admins)
# async def edit_sub(message: types.Message):
#     await message.answer('✏️ Enter ID:')
#     await editsub.user_id.set()
#
# @dp.message_handler(IsPrivateMessage(), state=editsub.user_id, chat_id=admins)
# async def editsub_user_id(message: types.Message, state: FSMContext):
#     answer = message.text
#     if answer.isnumeric():
#         await state.update_data(user_id=int(answer))
#         data = await state.get_data()
#         user_id = data.get('user_id')
#         user = await quick_commands.select_user(int(user_id))
#         sub = time_sub_day(db_sql.get_sub_time(user_id))
#         if sub == False:
#             sub = 'Not purchased'
#         markup = InlineKeyboardMarkup(row_width=2,
#                                       inline_keyboard=[
#                                           [
#                                               InlineKeyboardButton(text='1 month', callback_data='1m'),
#                                               InlineKeyboardButton(text='3 months', callback_data='3m'),
#                                               InlineKeyboardButton(text='6 months', callback_data='6m'),
#                                               InlineKeyboardButton(text='12 months', callback_data='12m'),
#                                           ],
#                                           [
#                                               InlineKeyboardButton(text='🗑 Delete', callback_data='delete'),
#                                               InlineKeyboardButton(text='❌ Cancel', callback_data='cancel3'),
#                                           ]
#                                       ])
#         await message.answer(f'<b>🆙 Editing of subscription:</b>\n\n'
#                              f'<b>ID:</b> {user_id}\n'
#                              f'<b>Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
#                              f'<b>Subscription:</b> {sub}',
#                              reply_markup=markup
#                              )
#     else:
#         await message.answer('⚠️ Enter correct ID.')
#
# @dp.callback_query_handler(text='1m', state=editsub.user_id, chat_id=admins)
# async def createuser_create(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     user = await quick_commands.select_user(user_id)
#     sub_time = int(time.time()) + days_to_seconds(30)
#     db_sql.set_sub_time(user_id, sub_time)
#     await call.message.answer(f'<b>🆙 {user.name} got a subscription for 1 month.</b>\n\n')
#     await state.finish()
#
# @dp.callback_query_handler(text='3m', state=editsub.user_id, chat_id=admins)
# async def createuser_create(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     user = await quick_commands.select_user(user_id)
#     sub_time = int(time.time()) + days_to_seconds(90)
#     db_sql.set_sub_time(user_id, sub_time)
#     await call.message.answer(f'<b>🆙 {user.name} got a subscription for 3 months.</b>\n\n')
#     await state.finish()
#
# @dp.callback_query_handler(text='6m', state=editsub.user_id, chat_id=admins)
# async def createuser_create(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     user = await quick_commands.select_user(user_id)
#     sub_time = int(time.time()) + days_to_seconds(180)
#     db_sql.set_sub_time(user_id, sub_time)
#     await call.message.answer(f'<b>🆙 {user.name} got a subscription for 6 months.</b>\n\n')
#     await state.finish()
#
# @dp.callback_query_handler(text='12m', state=editsub.user_id, chat_id=admins)
# async def createuser_create(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     user = await quick_commands.select_user(user_id)
#     sub_time = int(time.time()) + days_to_seconds(360)
#     db_sql.set_sub_time(user_id, sub_time)
#     await call.message.answer(f'<b>🆙 {user.name} got a subscription for 12 months.</b>\n\n')
#     await state.finish()
#
#
# @dp.callback_query_handler(text='delete', state=editsub.user_id, chat_id=admins)
# async def createuser_create(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     user = await quick_commands.select_user(user_id)
#     sub_time = '0'
#     db_sql.set_sub_time(user_id, sub_time)
#     await call.message.answer(f'<b>🗑 Subscription of {user.name} was deleted.</b>\n\n')
#     await state.finish()
#
# @dp.callback_query_handler(text='cancel3', state=editsub.user_id, chat_id=admins)
# async def createuser_cancel(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Editing of the subscription is cancelled.</b>')
#
