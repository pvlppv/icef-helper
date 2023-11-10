from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage, IsPrivateCallback, IsDatabaseUserCallback, IsAccepterUserCallback, \
    IsSubscriberChannelCallback
from keyboards.inline.inline_keyboard_homepage import ikb_homepage, ikb_homepage_back
from loader import dp
from utils.db_api import quick_commands


@dp.callback_query_handler(IsPrivateCallback(), IsDatabaseUserCallback(), IsAccepterUserCallback(), IsSubscriberChannelCallback(), text='homepage_contacts')
async def homepage_contacts(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>👨🏼‍💻 Contacts:</b>\n\n'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
                                 f'👤 <b>Owner:</b> @paoloppv'
                                 , reply_markup=ikb_homepage_back)

@dp.callback_query_handler(IsPrivateCallback(), IsDatabaseUserCallback(), IsAccepterUserCallback(), IsSubscriberChannelCallback(), text='homepage_features')
async def homepage_contacts(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🧩 ICEF Helper Features:</b>\n\n'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
                                 f'<b>🔒 Приватный доступ</b>\n'
                                 f'<b>🌐 Автоматическая регистрация</b>\n'
                                 f'<b>👤 Profile</b> - личный/чужой профиль с автоматически обновляющимся рейтингом\n'
                                 f'<b>🔎 Searching by interests</b> - поиск студентов по специализациям, факультативам, интересам\n'
                                 f'<b>🗣 Network</b> - все собранные в одном месте ICEF каналы, чаты, стикерпаки и прочее\n'
                                 f'<b>💋 Anonymous chat</b> - анонимный чат среди студентов МИЭФ\n'
                                 f'<b>🗞 News</b> - новости с icef.hse.ru и icefstudents.hse.ru\n'
                                 f'<b>🎫 Events</b> - ближайшие ICEF события\n'
                                 f'<b>☀️ Good Morning</b> - ежедневная утренняя сводка\n'
                                 f'<b>💠 Smart LMS</b> - автоматически обновляющееся хранилище учебных материалов по предметам (лекции, семинары, дз, книги, прошлые экзамены, преподаватели и их офисные часы) с платформы Smart LMS\n'
                                 f'<b>🗃 Handbook</b> - быстрый доступ к справочнику студента\n'
                                 f'<b>📂 Materials</b> - полезные материалы для учёбы и работы, собранные выпускниками\n'
                                 f'<b>🗓️ Schedule</b> - личное расписание пар с платформы HSE RUZ\n'
                                 f'<b>📚 Subjects Schedule</b> - расписание всех занятий по определённому предмету\n'
                                 f'<b>👨🏻‍🏫 Professors</b> - информация о профессорах и их расписание\n'
                                 f'<b>🚪 Locations</b> - расположение важных мест на Покровке\n'
                                 f'<b>⚙️ Settings</b> - настройки (настройка уведомлений, изменение профиля, репорт etc.)\n'
                                 f'<b>🔊 Рассылка</b> напоминаний, объявлений и прочего\n'
                                 f'<b>👨🏼‍💻 Admin Panel</b>\n'
                                 f'<b>⚠️ Анти-спам система</b>\n'
                                 f'<b>📋 Статистика бота</b>\n'
                                 f'<b>💠 Платформа Smart LMS</b> прямо из диалога с ботом', reply_markup=ikb_homepage_back)

@dp.callback_query_handler(IsPrivateCallback(), IsDatabaseUserCallback(), IsAccepterUserCallback(), IsSubscriberChannelCallback(), text='homepage_statistics')
async def homepage_statistics(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>📋 ICEF Helper Statistics:</b>\n\n'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
                                 f'<b>👼🏻 Created:</b> 01.08.2022\n\n'
                                 f'1️⃣ <b>1st course users:</b> {await quick_commands.count_users_1course()}\n'
                                 f'2️⃣ <b>2nd course users:</b> {await quick_commands.count_users_2course()}\n'
                                 f'3️⃣ <b>3rd course users:</b> {await quick_commands.count_users_3course()}\n'
                                 f'4️⃣ <b>4th course users:</b> {await quick_commands.count_users_4course()}\n\n'
                                 , reply_markup=ikb_homepage_back)

@dp.callback_query_handler(IsPrivateCallback(), IsDatabaseUserCallback(), IsAccepterUserCallback(), IsSubscriberChannelCallback(), text='homepage_back')
async def homepage_back(call: types.CallbackQuery):
    await call.message.edit_text('<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_homepage)

