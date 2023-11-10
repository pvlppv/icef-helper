from aiogram import types

from keyboards.inline import ikb_start
from keyboards.inline.inline_keyboard_subscription2 import ikb_subscription2
from loader import dp


# @rate_limit(limit=3, key='/info')
# @dp.message_handler(IsPrivateMessage(), text='/info')
# async def start(message: types.Message):
#     try:
#         await message.answer(f'🌎 This is <ins>ICEF Helper</ins>.', reply_markup=ikb_start)
#     except:
#         print(traceback.format_exc())

# @dp.callback_query_handler(text='back')
# async def back(call: types.CallbackQuery):
#     await call.message.edit_text(f'⭐️ Full access to the bot is only with the subscription.\n\n'
#                          f'Click the button below to learn more.', reply_markup=ikb_start)


@dp.callback_query_handler(text='sub')
async def sub(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>⭐️ Subscription to ICEF Helper:</b>\n\n'
                                  f'<b>Features:</b>\n'
                                  # f'🔒 Приватный доступ\n'
                                  # f'⭐️ Система платной подписки\n'
                                  f'👤 Profile - личный/чужой профиль с автоматически обновляющимся рейтингом\n'
                                  f'🗃 Handbook - быстрый доступ к справочнику студента\n'
                                  f'📂 Materials - полезные материалы по учёбе и работе\n'
                                  f'🗣 Chats - беседы по интересам\n'
                                  f'📚 Subjects - предметы с актуальной информацией по ним\n'
                                  f'🔔 Timetable - расписание пар у всех групп\n'
                                  f'🚪 Locations - расположение важных мест на Покровке\n'
                                  f'🗞 ICEF news - новости с icef.hse.ru с автоматической рассылкой\n'
                                  f'🎫 ICEF events - ближайшие ICEF события\n'
                                  f"⚙️ Settings - настройки (изменение профиля, репорт etc.)\n"
                                  # f"⚠️ Анти-спам система\n"
                                  f'🔊 Рассылка напоминалок, объявлений и прочего\n'
                                  f"💠 Платформа Smart LMS прямо из диалога с ботом\n\n"
                                  f'<b>Price:</b> 49 rub/month'
                         , reply_markup=ikb_subscription2)

# @dp.callback_query_handler(text='features')
# async def features(call: types.CallbackQuery):
#     await call.message.edit_text(f''
#                       f'<b>Features of ICEF Helper:</b>\n\n'
#                       # f'🔒 Приватный доступ\n'
#                       # f'⭐️ Система платной подписки\n'
#                       f'👤 Profile - личный/чужой профиль с автоматически обновляющимся рейтингом\n'
#                       f'🗃 Handbook - быстрый доступ к справочнику студента\n'
#                       f'📂 Materials - полезные материалы по учёбе и работе\n'
#                       f'🗣 Chats - беседы по интересам\n'
#                       f'📚 Subjects - предметы с актуальной информацией по ним\n'
#                       f'🔔 Timetable - расписание пар у всех групп\n'
#                       f'🚪 Locations - расположение важных мест на Покровке\n'
#                       f'🗞 ICEF news - новости с icef.hse.ru с автоматической рассылкой\n'
#                       f'🎫 ICEF events - ближайшие ICEF события\n'
#                       f"⚙️ Settings - настройки (изменение профиля, репорт etc.)\n"
#                       # f"⚠️ Анти-спам система\n"
#                       f'🔊 Рассылка напоминалок, объявлений и прочего\n'
#                       f"👤 Платформа Smart LMS прямо из диалога с ботом",
#                       reply_markup=ikb_start_features)

@dp.callback_query_handler(text='cancel2')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(f'⭐️ Full access to the bot is only with the subscription.\n\n'
                         f'Click the button below to learn more.', reply_markup=ikb_start)
