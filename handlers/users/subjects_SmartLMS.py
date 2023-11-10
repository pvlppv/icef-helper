import os

from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, IsSubscriberChannelMessage
from keyboards.default.keyboard_ICEFHelper import kb_studying
from keyboards.inline.inline_keyboard_SmartLMS import ikb_SmartLMS_subjects, ikb_SmartLMS_calculus, ikb_SmartLMS, \
    ikb_SmartLMS_statistics, ikb_SmartLMS_microeconomics, ikb_SmartLMS_history, ikb_SmartLMS_timetable, \
    ikb_SmartLMS_officehours, ikb_SmartLMS_optionalcourses, \
    ikb_SmartLMS_examstimetable
from loader import dp, db_sql
from utils.misc import rate_limit



@rate_limit(limit=3, key='💠 Smart LMS')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='💠 Smart LMS')
async def command_smartlms(message: types.Message):
    await message.answer(f'<b>💠 Smart LMS:</b>',
                         reply_markup=ikb_SmartLMS)

@dp.callback_query_handler(text='SmartLMS_back')
async def command_smartlms_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>💠 Smart LMS:</b>', reply_markup=ikb_SmartLMS)

@dp.callback_query_handler(text='SmartLMS_subjects')
async def command_SmartLMS_subjects(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_subjects)

@dp.callback_query_handler(text='SmartLMS_subjects_calculus')
async def command_subjects_calculus(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_calculus)

@dp.callback_query_handler(text='SmartLMS_subjects_calculus_classes')
async def command_subjects_calculus_classes(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus lectures:</b>')
    path = '/root/bot/media/Calculus'
    # path = '/Users/pavelpopov/Downloads/Calculus'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('Lecture'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_calculus_ha')
async def command_subjects_calculus_ha(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus HAs:</b>')
    path = '/root/bot/media/Calculus'
    # path = '/Users/pavelpopov/Downloads/Calculus'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('HA'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_calculus_other')
async def command_subjects_calculus_other(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus other:</b>')
    path = '/root/bot/media/Calculus'
    # path = '/Users/pavelpopov/Downloads/Calculus'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if not f.__contains__('Lecture') and not f.__contains__('HA'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_calculus_back')
async def command_SmartLMS_subjects_calculus_back(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_subjects)

@dp.callback_query_handler(text='SmartLMS_subjects_statistics')
async def command_subjects_statistics(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_statistics)

@dp.callback_query_handler(text='SmartLMS_subjects_statistics_classes')
async def command_subjects_statistics_classes(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics lectures:</b>')
    path = '/root/bot/media/Statistics'
    # path = '/Users/pavelpopov/Downloads/Statistics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('lecture'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_statistics_ha')
async def command_subjects_statistics_ha(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics HAs:</b>')
    path = '/root/bot/media/Statistics'
    # path = '/Users/pavelpopov/Downloads/Statistics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('ha'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_statistics_other')
async def command_subjects_statistics_other(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics other:</b>')
    path = '/root/bot/media/Statistics'
    # path = '/Users/pavelpopov/Downloads/Statistics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if not f.__contains__('lecture') and not f.__contains__('ha'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_statistics_back')
async def command_SmartLMS_subjects_statistics_back(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_subjects)

@dp.callback_query_handler(text='SmartLMS_subjects_microeconomics')
async def command_subjects_microeconomics(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_microeconomics)

@dp.callback_query_handler(text='SmartLMS_subjects_microeconomics_classes')
async def command_subjects_microeconomics_classes(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics lectures:</b>')
    path = '/root/bot/media/Microeconomics'
    # path = '/Users/pavelpopov/Downloads/Microeconomics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('Lecture'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_microeconomics_ha')
async def command_subjects_microeconomics_ha(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics HAs:</b>')
    path = '/root/bot/media/Microeconomics'
    # path = '/Users/pavelpopov/Downloads/Microeconomics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('HW'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_microeconomics_other')
async def command_subjects_microeconomics_other(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics other:</b>')
    path = '/root/bot/media/Microeconomics'
    # path = '/Users/pavelpopov/Downloads/Microeconomics'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if not f.__contains__('Lecture') and not f.__contains__('HW'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_microeconomics_back')
async def command_SmartLMS_subjects_microeconomics_back(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_subjects)

@dp.callback_query_handler(text='SmartLMS_subjects_history')
async def command_subjects_history(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_history)

@dp.callback_query_handler(text='SmartLMS_subjects_history_classes')
async def command_subjects_history_classes(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History lectures:</b>')
    path = '/root/bot/media/History'
    # path = '/Users/pavelpopov/Downloads/History'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('Lecture'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_history_ha')
async def command_subjects_history_ha(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History HAs:</b>')
    path = '/root/bot/media/History'
    # path = '/Users/pavelpopov/Downloads/History'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if f.__contains__('HA'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_history_other')
async def command_subjects_history_other(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History other:</b>')
    path = '/root/bot/media/History'
    # path = '/Users/pavelpopov/Downloads/History'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        if not f.__contains__('Lecture') and not f.__contains__('HA'):
            await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_subjects_history_back')
async def command_SmartLMS_subjects_history_back(call: types.CallbackQuery):
    count_calculus = str(db_sql.calculus_last_count())[2:-3]
    count_statistics = str(db_sql.statistics_last_count())[2:-3]
    count_microeconomics = str(db_sql.microeconomics_last_count())[2:-3]
    count_history = str(db_sql.history_last_count())[2:-3]

    last_update_calculus = str(db_sql.calculus_last_update()).replace("'", "")
    last_update_calculus2 = last_update_calculus.replace('.000', '')

    last_update_statistics = str(db_sql.statistics_last_update()).replace("'", "")
    last_update_statistics2 = last_update_statistics.replace('.000', '')

    last_update_microeconomics = str(db_sql.microeconomics_last_update()).replace("'", "")
    last_update_microeconomics2 = last_update_microeconomics.replace('.000', '')

    last_update_history = str(db_sql.history_last_update()).replace("'", "")
    last_update_history2 = last_update_history.replace('.000', '')
    await call.message.edit_text(f'<b>📚 Subjects:</b>\n\n'
                                 # f'<b>Updated:</b> {last_update[3:-4]}\n\n'
                                 f'<b>📘 Calculus:</b>\n'
                                 f'<b>Amount of files:</b> {count_calculus}\n'
                                 f'<b>Last update:</b> {last_update_calculus2[1:-1]}\n\n'
                                 f'<b>📗 Statistics:</b>\n'
                                 f'<b>Amount of files:</b> {count_statistics}\n'
                                 f'<b>Last update:</b> {last_update_statistics2[1:-1]}\n\n'
                                 f'<b>📙 Microeconomics:</b>\n'
                                 f'<b>Amount of files:</b> {count_microeconomics}\n'
                                 f'<b>Last update:</b> {last_update_microeconomics2[1:-1]}\n\n'
                                 f'<b>📔 History:</b>\n'
                                 f'<b>Amount of files:</b> {count_history}\n'
                                 f'<b>Last update:</b> {last_update_history2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_subjects)

@dp.callback_query_handler(text='SmartLMS_timetable')
async def command_SmartLMS_timetable(call: types.CallbackQuery):
    last_update_timetable = str(db_sql.timetable_last_update()).replace("'", "")
    last_update_timetable2 = last_update_timetable.replace('.000', '')
    await call.message.edit_text(f'<b>🕓 Timetable:</b>\n\n'
                                 f'<b>Last update:</b> {last_update_timetable2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_timetable)

@dp.callback_query_handler(text='SmartLMS_timetable_timetable_show')
async def command_timetable_timetable_show(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🕓 Timetable:</b>')
    path = '/root/bot/media/Timetable/Timetable'
    # path = '/Users/pavelpopov/Downloads/Timetable/Timetable'
    files = []
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_officehours')
async def command_SmartLMS_officehours(call: types.CallbackQuery):
    last_update_office_hours = str(db_sql.office_hours_last_update()).replace("'", "")
    last_update_office_hours2 = last_update_office_hours.replace('.000', '')
    await call.message.edit_text(f'<b>👨🏼‍🏫 Office hours:</b>\n\n'
                                 f'<b>Last update:</b> {last_update_office_hours2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_officehours)

@dp.callback_query_handler(text='SmartLMS_timetable_officehours_show')
async def command_timetable_officehours_show(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>👨🏼‍🏫 Office hours:</b>')
    path = '/root/bot/media/Timetable/Office hours'
    # path = '/Users/pavelpopov/Downloads/Timetable/Office hours'
    files = []
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_optionalcourses')
async def command_SmartLMS_optionalcourses(call: types.CallbackQuery):
    last_update_optional_courses = str(db_sql.optional_courses_last_update()).replace("'", "")
    last_update_optional_courses2 = last_update_optional_courses.replace('.000', '')
    await call.message.edit_text(f'<b>🔭 Optional courses:</b>\n\n'
                                 f'<b>Last update:</b> {last_update_optional_courses2[1:-1]}\n\n'
                                 , reply_markup=ikb_SmartLMS_optionalcourses)

@dp.callback_query_handler(text='SmartLMS_timetable_optionalcourses_show')
async def command_timetable_optionalcourses_show(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🔭 Optional courses:</b>')
    path = '/root/bot/media/Timetable/Optional courses'
    # path = '/Users/pavelpopov/Downloads/Timetable/Optional courses'
    files = []
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")

@dp.callback_query_handler(text='SmartLMS_examstimetable')
async def command_SmartLMS_examstimetable(call: types.CallbackQuery):
    last_update_exams_timetable = str(db_sql.exams_timetable_last_update()).replace("'", "")
    last_update_exams_timetable2 = last_update_exams_timetable.replace('.000', '')
    await call.message.edit_text(f'<b>📖 Exams timetable:</b>\n\n'
                                 f'<b>Last update:</b> {last_update_exams_timetable2[1:-1]}'
                                 , reply_markup=ikb_SmartLMS_examstimetable)

@dp.callback_query_handler(text='SmartLMS_timetable_examstimetable_show')
async def command_timetable_examstimetable_show(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>📖 Exams timetable:</b>')
    path = '/root/bot/media/Timetable/Exams timetable'
    # path = '/Users/pavelpopov/Downloads/Timetable/Exams timetable'
    files = []
    for r, d, f in os.walk(path):
        f.sort()
        for file in f:
            files.append(os.path.join(r, file))
    for f in files:
        await dp.bot.send_document(chat_id=call.from_user.id, document=open(f, 'rb'))
    await call.message.answer("<b>That's it for now.</b>")


