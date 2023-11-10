import traceback

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import admins, moderators
from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
# from handlers.users.rating_main_parsing import collect_data
from keyboards.default import kb_changeprofile, kb_settings3
from keyboards.default.keyboard_ICEFHelper import kb_ICEFHelperMenu
from keyboards.default.keyboard_settings import kb_settings, kb_settings2
from keyboards.inline.inline_keyboard_editprofile import ikb_editprofile
from keyboards.inline.inline_keyboard_settings import ikb_settings, ikb_settings_admins, \
    ikb_settings_admins_back, ikb_morning_settings2, ikb_morning_settings, ikb_notification_settings2, \
    ikb_notification_settings
from loader import dp
from states import changeprofile, report
from states.morning_time import morning_time
from utils.db_api import quick_commands
from utils.db_api.quick_commands import select_user_specialization, select_user_additional_courses, select_user_sport, \
    select_user_academic_group, select_user_course, select_user_notification_status, select_user_email, \
    select_user_morning_status, select_user_morning_time
from utils.misc import rate_limit
from aiogram.utils.json import json
from aiogram.utils.markdown import hbold
import ruz.utils



@dp.callback_query_handler(text='homepage_settings')
async def command_settings_new(call: types.CallbackQuery):
    user = await quick_commands.select_user(call.from_user.id)
    if user.notification_status == 'Off':
        a = user.specialization and user.additional_courses and user.sport
        if a is None:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
        else:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
    else:
        a = user.specialization and user.additional_courses and user.sport
        if a is None:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
        else:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)

#morning
@dp.callback_query_handler(text='morning_settings')
async def morning_settings(call: types.CallbackQuery):
    user = await quick_commands.select_user(call.from_user.id)
    if user.morning_status == 'Off':
        await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                     f'<b>🌤 Good Morning:</b> [OFF]'
                                     f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)
    else:
        await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                     f'<b>☀️ Good Morning:</b> [ON]'
                                     f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)

@dp.callback_query_handler(text='morning_notification_back')
async def morning_notification_back(call: types.CallbackQuery):
    user = await quick_commands.select_user(call.from_user.id)
    if user.notification_status == 'Off':
        a = user.specialization and user.additional_courses and user.sport
        if a is None:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
        else:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔕 Notifications:</b> [OFF]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
    else:
        a = user.specialization and user.additional_courses and user.sport
        if a is None:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
        else:
            if user.morning_status == 'Off':
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>🌤 Good Morning:</b> [OFF]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)
            else:
                await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                             f'<b>👤 Profile:</b> [FULL]\n'
                                             f'<b>☀️ Good Morning:</b> [ON]\n'
                                             f'<b>🔔 Notifications:</b> [ON]'
                                             f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_settings)

@dp.callback_query_handler(text='morning_off')
async def morning_off(call: types.CallbackQuery):
    morning_status = await select_user_morning_status(call.from_user.id)
    await morning_status.update(morning_status='Off').apply()
    await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                 f'<b>🌤 Good Morning:</b> [OFF]'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)

@dp.callback_query_handler(text='morning_on')
async def morning_on(call: types.CallbackQuery):
    morning_status = await select_user_morning_status(call.from_user.id)
    await morning_status.update(morning_status='On').apply()
    await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                 f'<b>☀️ Good Morning:</b> [ON]'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)

# @dp.callback_query_handler(text='morning_time')
# async def command_morning_time(call: types.CallbackQuery):
#     await call.message.answer('Enter your time for Good Morning:\n\n'
#                               '<i>Default: 08:00</i>')
#     await morning_time.time.set()
#
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=morning_time.time)
# async def command_morning_timetwo(message: types.Message, state: FSMContext):
#     morning_time = await select_user_morning_time(message.from_user.id)
#     answer = message.text
#     if answer.__contains__(':'):
#         await morning_time.update(morning_time=answer).apply()
#         await message.answer(f"<b>☀️ You've set {answer} for Good Morning.</b>")
#         await state.finish()
#     else:
#         await message.answer('⚠️ Enter correct time.')
#
# @dp.callback_query_handler(text='morning_settings')
# async def command_morning_settings(call: types.CallbackQuery):
#     user = await quick_commands.select_user(call.from_user.id)
#     if user.notification_status == 'Off':
#         a = user.specialization and user.additional_courses and user.sport
#         if a is None:
#             if user.morning_status == 'Off':
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
#                                              f'<b>🌤 Good Morning:</b> [OFF]\n'
#                                              f'<b>🔕 Notifications:</b> [OFF]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)
#             else:
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
#                                              f'<b>☀️ Good Morning:</b> [ON]\n'
#                                              f'<b>🔕 Notifications:</b> [OFF]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)
#         else:
#             if user.morning_status == 'Off':
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [FULL]\n'
#                                              f'<b>🌤 Good Morning:</b> [OFF]\n'
#                                              f'<b>🔕 Notifications:</b> [OFF]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)
#             else:
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [FULL]\n'
#                                              f'<b>☀️ Good Morning:</b> [ON]\n'
#                                              f'<b>🔕 Notifications:</b> [OFF]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)
#     else:
#         a = user.specialization and user.additional_courses and user.sport
#         if a is None:
#             if user.morning_status == 'Off':
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
#                                              f'<b>🌤 Good Morning:</b> [OFF]\n'
#                                              f'<b>🔔 Notifications:</b> [ON]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)
#             else:
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [NOT FULL] (add missing data in your profile)\n'
#                                              f'<b>☀️ Good Morning:</b> [ON]\n'
#                                              f'<b>🔔 Notifications:</b> [ON]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)
#         else:
#             if user.morning_status == 'Off':
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [FULL]\n'
#                                              f'<b>🌤 Good Morning:</b> [OFF]\n'
#                                              f'<b>🔔 Notifications:</b> [ON]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings2)
#             else:
#                 await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
#                                              f'<b>👤 Profile:</b> [FULL]\n'
#                                              f'<b>☀️ Good Morning:</b> [ON]\n'
#                                              f'<b>🔔 Notifications:</b> [ON]'
#                                              f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_morning_settings)


# notifications
@dp.callback_query_handler(text='notifications_settings')
async def notification_settings(call: types.CallbackQuery):
    user = await quick_commands.select_user(call.from_user.id)
    if user.notification_status == 'Off':
        await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                     f'<b>🔕 Notifications:</b> [OFF]'
                                     f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_notification_settings2)
    else:
        await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                     f'<b>🔔 Notifications:</b> [ON]'
                                     f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_notification_settings)

@dp.callback_query_handler(text='notifications_on')
async def command_notifications_on(call: types.CallbackQuery):
    notification_status = await select_user_notification_status(call.from_user.id)
    await notification_status.update(notification_status='On').apply()
    await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                 f'<b>🔔 Notifications:</b> [ON]'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>',
                                 reply_markup=ikb_notification_settings)

@dp.callback_query_handler(text='notifications_off')
async def command_notifications_off(call: types.CallbackQuery):
    notification_status = await select_user_notification_status(call.from_user.id)
    await notification_status.update(notification_status='Off').apply()
    await call.message.edit_text(f'<b>⚙️ Settings:</b>\n\n'
                                 f'<b>🔕 Notifications:</b> [OFF]'
                                 f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>',
                                 reply_markup=ikb_notification_settings2)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='analytics')
async def command_analytics(message: types.Message):
    await message.answer('analytics')

# user settings
# editing of profile
@dp.callback_query_handler(text='editprofile')
async def command_edit_profile(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🆕 Editing of the profile:</b>', reply_markup=ikb_editprofile)

@rate_limit(limit=3, key='👤 Name')
@dp.callback_query_handler(text='editprofile_name')
async def command_edit_name(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new name (Имя Фамилия):\n\n'
                              f'<em>Example: Алла Фридман</em>'
                              )
    await changeprofile.name.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.name)
async def command_newname(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct name.')
    else:
        await state.update_data(name=answer)
        data = await state.get_data()
        name = data.get('name')
        name1 = await select_user_sport(message.from_user.id)
        await name1.update(name=answer).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>👤 New name:</b> {name}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)

@dp.callback_query_handler(text='editprofile_email')
async def command_edit_email(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new email (email@edu.hse.ru):\n\n')
    await changeprofile.email.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.email)
async def command_newemail(message: types.Message, state: FSMContext):
    answer = message.text
    is_hse_email = ruz.utils.is_hse_email(email=answer)
    is_valid_hse_email = ruz.utils.is_valid_hse_email(email=answer)
    if is_hse_email + is_valid_hse_email:
        await state.update_data(email=answer)
        data = await state.get_data()
        email = data.get('email')
        email1 = await select_user_email(message.from_user.id)
        await email1.update(email=answer).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>📧 New email:</b> {email}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)
    else:
        await message.answer('⚠️ Enter correct HSE email.')

@dp.callback_query_handler(text='editprofile_course')
async def command_edit_course(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new course (1-4):')
    await changeprofile.course.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.course)
async def command_newcourse(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await state.update_data(course=int(answer))
        data = await state.get_data()
        course = data.get('course')
        course1 = await select_user_course(message.from_user.id)
        await course1.update(course=int(answer)).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>👥 New course:</b> {course}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)
    else:
        await message.answer('⚠️ Enter correct course.')

@dp.callback_query_handler(text='editprofile_academic_group')
async def command_edit_academicgroup(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new academic group (1-11):\n\n')
    await changeprofile.academic_group.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.academic_group)
async def command_newacademicgroup(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        if int(answer) < 12:
            if int(answer) > 0:
                await state.update_data(academic_group=int(answer))
                data = await state.get_data()
                academic_group = data.get('academic_group')
                academic_group1 = await select_user_academic_group(message.from_user.id)
                await academic_group1.update(academic_group=int(answer)).apply()
                await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                                     f'<b>👥 New academic group:</b> {academic_group}')
                await state.finish()
                await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)
            else:
                await message.answer('⚠️ Enter correct academic group number.')
        else:
            await message.answer('⚠️ Enter correct academic group number.')
    else:
        await message.answer('⚠️ Enter correct academic group.')

@dp.callback_query_handler(text='editprofile_specialization')
async def command_edit_specialization(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new specialization:\n\n'
                         f'<em>Example: Экономика и финансы</em>\n\n'
                         f'🏦 Банковское дело и финансы\n'
                         f'💵 Экономика и менеджмент\n'
                         f'💴 Экономика\n'
                         f'💶 Экономика и финансы\n'
                         f'🗄 Бухгалтерский учёт и финансы\n'
                         f'💷 Экономика и математика'
                         )
    await changeprofile.specialization.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.specialization)
async def command_newspecialization(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct specialization.')
    else:
        await state.update_data(specialization=answer)
        data = await state.get_data()
        specialization = data.get('specialization')
        specialization1 = await select_user_specialization(message.from_user.id)
        await specialization1.update(specialization=answer).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>💼 New specialization:</b> {specialization}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)

@dp.callback_query_handler(text='editprofile_additional_courses')
async def command_edit_additionalcourses(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new additional courses:\n\n'
                         f'<em>Example: Python, Trading, Gym</em>\n\n'
                         f'🐍 Python\n'
                         f'💿 C#\n'
                         f'📊 Excel\n'
                         f'📈 Trading\n'
                         f'🎵 Music\n'
                         f'🇫🇷 French\n'
                         f'🇮🇹 Italian\n'
                         f'🇩🇪 Deutsch\n'
                         f'🇪🇸 Spanish\n'
                         f'🇨🇳 Chinese\n'
                         f'🇦🇪 Arabic\n'
                         f'🏋️ Gym\n'
                         f'🧘 Yoga'
                         )
    await changeprofile.additional_courses.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.additional_courses)
async def command_newadditionalcourses(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct additional courses.')
    else:
        await state.update_data(additional_courses=answer)
        data = await state.get_data()
        additional_courses = data.get('additional_courses')
        additional_courses1 = await select_user_additional_courses(message.from_user.id)
        await additional_courses1.update(additional_courses=answer).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>🔭 New additional courses:</b> {additional_courses}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)

@dp.callback_query_handler(text='editprofile_sport')
async def command_edit_sport(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter new sport:\n\n'
                         f'<em>Example: Soccer, Basketball, Cycling</em>\n\n'
                         f'⚽️ Soccer\n'
                         f'🏀 Basketball\n'
                         f'🎾 Tennis\n'
                         f'🏐 Volleyball\n'
                         f'🏒 Hockey\n'
                         f'🏊 Swimming\n'
                         f'🤸 Gymnastics\n'
                         f'🚴 Cycling\n'
                         f'- etc.'
                         )
    await changeprofile.sport.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=changeprofile.sport)
async def command_newsport(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct sport.')
    else:
        await state.update_data(sport=answer)
        data = await state.get_data()
        sport = data.get('sport')
        sport1 = await select_user_sport(message.from_user.id)
        await sport1.update(sport=answer).apply()
        await message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                             f'<b>🎱 New sport:</b> {sport}')
        await state.finish()
        await message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)

@dp.callback_query_handler(text='editprofile_username')
async def command_newusername(call: types.CallbackQuery):
    username = f'https://t.me/' + call.from_user.username
    username1 = await select_user_sport(call.from_user.id)
    await username1.update(username=username).apply()
    await call.message.answer(f"<b>🆕 You've edited your profile.</b>\n\n"
                              f'<b>🔰 New username:</b> @{call.from_user.username}')
    await call.message.answer(f'🆕 Editing of the profile:', reply_markup=ikb_editprofile)

@dp.callback_query_handler(text='editprofile_back')
async def command_editprofile_back(call: types.CallbackQuery):
    try:

        # collect_data()

        markup = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='✏️ Edit profile', callback_data='editprofile'),
                                          ],
                                          [
                                              InlineKeyboardButton(text='⬅️ Back', callback_data='profile_back')
                                          ]
                                      ])
        user = await quick_commands.select_user(call.from_user.id)
        student = user.name
        # sub = time_sub_day(db_sql.get_sub_time(call.from_user.id))
        # if sub == False:
        #     sub = 'None'
        profile = (f'<b>👤 Profile:</b>\n\n <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>'
                   f'<b>👤 Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
                   f'      <b>👥 Course:</b> {user.course}\n'
                   f'      <b>🫂 Academic group:</b> {user.academic_group}\n'
                   # f'      <b>🇬🇧 English group:</b> {user.english_group}\n'
                   f'      <b>💼 Specialization:</b> {user.specialization}\n'
                   f'      <b>🔭 Additional courses:</b> {user.additional_courses}\n'
                   f'      <b>🎱 Sport:</b> {user.sport}'
                   )

        # with open('/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/result_data.json') as file:
        with open("/root/bot/handlers/users/result_data.json") as file:
            data = json.load(file)

        for item in data:
            if item["name"] == student:
                await call.message.edit_text(f"{profile}\n"
                                     f"      {hbold('🏆 Rating position:')} {item.get('place')}\n" \
                                     f"      {hbold('🧷 Average score:')} {item.get('average')}\n" \
                                     f"      {hbold('🔗 Minimum score:')} {item.get('min')}\n" \
                                     f"      {hbold('📎 Percentile:')} {item.get('percentile')}\n" \
                                     f"      {hbold('🖇 GPA:')} {item.get('gpa')}\n\n" \
                                     # f'<b>⭐️ Subscription:</b> {sub}\n\n'
                                     f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}', reply_markup=markup)
                break
        else:
            await call.message.edit_text(f'{profile}\n'
                                         f'      [Нет данных о рейтинге]\n'
                                         f'      <b>🏆 Rating position:</b> None\n'
                                         f'      <b>🧷 Average score:</b> None\n'
                                         f'      <b>🔗 Minimum score:</b> None\n'
                                         f'      <b>📎 Percentile:</b> None\n'
                                         f'      <b>🖇 GPA:</b> None\n\n'
                                         # f'<b>⭐️ Subscription:</b> {sub}\n\n'
                                         f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}', reply_markup=markup)
    except AttributeError:
        await call.message.edit_text("<b>🌐 You're not registered.</b>\n\n"
                             'Click the button below to register and enter to the bot. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_registration)
    except:
        print(traceback.format_exc())

# update menu
@dp.callback_query_handler(text='update_menu')
async def command_updatemenu(call: types.CallbackQuery):
    await call.message.answer('⌨️ Menu has been updated.', reply_markup=kb_ICEFHelperMenu)

# report
@dp.callback_query_handler(text='report')
async def command_report(call: types.CallbackQuery):
    await call.message.answer('✏️ Enter a report:')
    await report.report.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=report.report)
async def command_report_state(message: types.Message, state: FSMContext):
    answer = message.text
    answer2 = message.from_user.username
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='✅ Send', callback_data='send'),
                                          InlineKeyboardButton(text='🔄 Rechange', callback_data='rechange'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel'),
                                      ]
                                  ])
    await state.update_data(report=answer)
    await state.update_data(username=answer2)
    await message.answer(text=f'ℹ️ <b>Report:</b> {answer}', reply_markup=markup)

@dp.callback_query_handler(text='send', state=report.report)
async def command_report_send(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    report = data.get('report')
    username = data.get('username')
    # user = await quick_commands.select_all_users()
    await state.finish()
    await call.message.edit_text(f'ℹ️ <b>Your report has been sent to admins.</b>\n\n'
                              f'Report: <em>{report}</em>')
    for moderator in moderators:
        await dp.bot.send_message(chat_id=moderator, text=f'ℹ️ Report from @{username}: {report}')

@dp.callback_query_handler(text='rechange', state=report.report)
async def command_report_rechange(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(f'✏️ Enter a new report:')
    await report.report.set()

@dp.callback_query_handler(text='cancel', state=report.report)
async def command_report_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>ℹ️ Your report has been cancelled.</b>')
