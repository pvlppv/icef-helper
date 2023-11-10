import traceback

from aiogram import types
from aiogram.dispatcher.filters import Command, state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import time

from data.config import admins, moderators, admin
from filters import IsPrivateMessage
# from handlers.users.subscription import days_to_seconds
from filters.IsSubscriberChannel import markup
from keyboards.default import kb_changeprofile
from keyboards.default.keyboard_ICEFHelper import kb_ICEFHelperMenu
from keyboards.default.keyboard_settings import kb_settings, kb_settings2
from keyboards.inline.inline_keyboard_settings import ikb_settings_admins_back
from loader import dp, bot, db_sql
from states import changeprofile, report, createuser, deleteuser, updateuser
from states.registration import accept_registration, decline_registration
from utils.db_api import quick_commands
from utils.db_api.quick_commands import select_user_specialization, select_user_additional_courses, select_user_sport, \
    new_user, select_all_users, count_users_1course, select_user_name, delete_user, select_user_created_at
from utils.misc import rate_limit
from datetime import timezone, datetime, timedelta


# создание юзера
@dp.message_handler(IsPrivateMessage(), text='/createuser', chat_id=admins)
async def command_createuser(message: types.Message):
    await message.answer('✏️ Enter ID:')
    await createuser.user_id.set()

@dp.message_handler(IsPrivateMessage(), state=createuser.user_id, chat_id=admins)
async def createuser_user_id(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await state.update_data(user_id=answer)
        await message.answer('✏️ Enter "Имя Фамилия":')
        await createuser.name.set()
    else:
        await message.answer('⚠️ Enter correct ID.')

@dp.message_handler(IsPrivateMessage(), state=createuser.name, chat_id=admins)
async def createuser_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct "Имя Фамилия".')
    else:
        await state.update_data(name=answer)
        await message.answer('✏️ Enter username-URL:')
        await createuser.username.set()

@dp.message_handler(IsPrivateMessage(), state=createuser.username, chat_id=admins)
async def createuser_username(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct username-URL.')
    else:
        await state.update_data(username=answer)
        await message.answer('✏️ Enter course:')
        await createuser.course.set()

@dp.message_handler(IsPrivateMessage(), state=createuser.course, chat_id=admins)
async def createuser_course(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await state.update_data(course=answer)
        await message.answer('✏️ Enter academic group:')
        await createuser.academic_group.set()
    else:
        await message.answer('⚠️ Enter correct course number.')

@dp.message_handler(IsPrivateMessage(), state=createuser.academic_group, chat_id=admins)
async def createuser_course(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='✅ Create', callback_data='create'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel'),
                                      ]
                                  ])
    if answer.isnumeric():
        await state.update_data(academic_group=answer)
        data = await state.get_data()
        user_id = data.get('user_id')
        name = data.get('name')
        username = data.get('username')
        course = data.get('course')
        academic_group = data.get('academic_group')
        await message.answer(text=f'▶️ Creating of the user:\n\n'
                                  f'<b>ID:</b> <code>{user_id}</code>\n'
                                  f'<b>Username:</b> {username}\n'
                                  f'<b>Name:</b> {name}\n'
                                  f'<b>Course:</b> {course}\n'
                                  f'<b>Academic group:</b> {academic_group}\n',
                                  reply_markup=markup)
    else:
        await message.answer('⚠️ Enter correct academic number.')

# @dp.message_handler(IsPrivateMessage(), state=createuser.english_group, chat_id=admins)
# async def createuser_group(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Create', callback_data='create'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='cancel'),
#                                       ]
#                                   ])
#     if answer.isnumeric():
#         await state.update_data(english_group=answer)
#         data = await state.get_data()
#         user_id = data.get('user_id')
#         name = data.get('name')
#         username = data.get('username')
#         course = data.get('course')
#         academic_group = data.get('academic_group')
#         english_group = data.get('english_group')
#         await message.answer(text=f'▶️ Creating of the user:\n\n'
#                                   f'<b>ID:</b> {user_id}\n'
#                                   f'<b>Username:</b> {username}\n'
#                                   f'<b>Name:</b> {name}\n'
#                                   f'<b>Course:</b> {course}\n'
#                                   f'<b>Academic group:</b> {academic_group}\n'
#                                   f'<b>English group:</b> {english_group}',
#                                   reply_markup=markup)
#     else:
#         await message.answer('⚠️ Enter correct english group number.')


@dp.callback_query_handler(text='create', state=createuser.academic_group, chat_id=admins)
async def createuser_create(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    name = data.get('name')
    username = data.get('username')
    course = data.get('course')
    academic_group = data.get('academic_group')
    await new_user(user_id=int(user_id), name=str(name), username=str(username), course=int(course), academic_group=int(academic_group), specialization='None', additional_courses='None', sport='None', status='None')
    await call.message.answer(f'<b>▶️ "{name}" was created.</b>\n\n')
    await state.finish()

@dp.callback_query_handler(text='cancel', state=createuser.academic_group, chat_id=admins)
async def createuser_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>❌ Creation of the user is cancelled.</b>')



# удаление юзера
@dp.message_handler(IsPrivateMessage(), text='/deleteuser', chat_id=admins)
async def command_deleteuser(message: types.Message):
    await message.answer('✏️ Enter "Имя Фамилия":')
    await deleteuser.name.set()

@dp.message_handler(IsPrivateMessage(), state=deleteuser.name, chat_id=admins)
async def deleteuser_name(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='✅ Delete', callback_data='delete'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel'),
                                      ]
                                  ])
    await state.update_data(name=answer)
    data = await state.get_data()
    name = data.get('name')
    user = await select_user_name(name)
    await message.answer(f'<b>◀️ Deleting of the user:</b>\n\n'
                         f'<b>ID:</b> <code>{user.user_id}</code>\n'
                         f'<b>Username:</b> {user.username}\n'
                         f'<b>Name:</b> {user.name}\n'
                         f'<b>Course:</b> {user.course}\n'
                         f'<b>Academic group:</b> {user.academic_group}\n'
                         f'<b>Specialization:</b> {user.specialization}\n'
                         f'<b>Additional courses:</b> {user.additional_courses}\n'
                         f'<b>Sport:</b> {user.sport}\n'
                         f'<b>Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}',
                         reply_markup=markup)

@dp.callback_query_handler(text='delete', state=deleteuser.name, chat_id=admins)
async def deleteuser_delete(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    if name.isnumeric():
        await call.message.answer('⚠️ Enter correct "Имя Фамилия".')
    else:
        user = await select_user_name(name)
        student = user.name
        await delete_user(student)
        await call.message.answer(f'<b>◀️ "{name}" was deleted.</b>\n\n')
        await state.finish()

@dp.callback_query_handler(text='cancel', state=deleteuser.name, chat_id=admins)
async def deleteuser_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>❌ Deleting of the user is cancelled.</b>')



# просмотр количества юзеров
# @dp.message_handler(IsPrivateMessage(), text='/allusers', chat_id=moderators)
# async def command_allusers(message: types.Message):
#     countusers = await count_users_1course()
#     await message.answer(f'<b>🚻 All users:</b> {countusers}')



# обновление какой-либо колонки юзера
# @dp.message_handler(IsPrivateMessage(), text='/updateuser', chat_id=admins)
# async def command_updateuser(message: types.Message):
#     await message.answer(f'✏️ Enter "created_at" date:')
#     await updateuser.created_at.set()
#
# @dp.message_handler(IsPrivateMessage(), state=updateuser.created_at, chat_id=admins)
# async def new_created_at(message: types.Message, state: FSMContext):
#     answer = datetime.date(message.text)
#     await state.update_data(created_at=answer)
#     data = await state.get_data()
#     created_at = data.get('created_at')
#     created_at1 = await select_user_created_at(message.from_user.id)
#     await created_at1.update(created_at=answer).apply()
#     await message.answer(f'<b>🔄 New "created_at":</b> {created_at}\n')
#     await state.finish()



# одобрение заявки юзера
@dp.callback_query_handler(text='edit_registrations')
async def check_registrations(call: types.CallbackQuery):
    try:
        reg = await quick_commands.select_unregistered()
        markup = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='✅ Accept', callback_data='accept_accept'),
                                              InlineKeyboardButton(text='❌ Decline', callback_data='decline_accept'),
                                          ]
                                      ])
        if reg:
            await call.message.answer(f'<b>▶️ Accepting of the user:</b>\n\n'
                                 f'<b>ID:</b> <code>{reg.user_id}</code>\n'
                                 f'<b>Username:</b> {reg.username}\n'
                                 f'<b>Name:</b> {reg.name}\n'
                                 f'<b>Course:</b> {reg.course}\n'
                                 f'<b>Academic group:</b> {reg.academic_group}\n'
                                 f'<b>Specialization:</b> {reg.specialization}\n'
                                 f'<b>Additional courses:</b> {reg.additional_courses}\n'
                                 f'<b>Sport:</b> {reg.sport}\n'
                                 f'<b>Registered:</b> {reg.created_at.strftime(format="%d.%m.%Y %H:%M")}',
                                 reply_markup=markup)
        else:
            await call.message.edit_text('<b>🌐 Editing of registrations:\n\nThere are no new registrations.</b>', reply_markup=ikb_settings_admins_back)
    except AttributeError:
        pass


@dp.callback_query_handler(text='accept_accept', chat_id=moderators)
async def accept_accept(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter ID to accept:')
    await accept_registration.user_id.set()

@dp.message_handler(state=accept_registration.user_id, chat_id=moderators)
async def accept(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        user = await quick_commands.select_user(message.from_user.id)
        reg = await quick_commands.select_unregistered()
        user1 = await quick_commands.select_user(int(message.text))
        if user1:
            await quick_commands.accept_registration(int(message.text))
            await dp.bot.send_message(chat_id=reg.user_id, text='<b>🌐 Your registration has been <ins>accepted</ins>.</b>\n\n', reply_markup=kb_ICEFHelperMenu)
            await dp.bot.send_message(chat_id=reg.user_id, text="🌐 Subscribe to the bot's channel to check all latest news and updates: https://t.me/+DFuYOJt5rcpjMWZi.", reply_markup=markup)
            for moderator in moderators:
                await dp.bot.send_message(chat_id=moderator, text=f'<b>▶️ Registration of "<code>{reg.name}</code>" has been <ins>accepted</ins> by the admin "{user.name}".</b>')
        else:
            await message.answer('⚠️ Wrong ID.')
    except AttributeError:
        await message.answer('⚠️ Wrong ID.')
    # if db_sql.user_exists(reg.user_id):
    #     sub_time = int(time.time()) + days_to_seconds(30)
    #     db_sql.set_sub_time(reg.user_id, sub_time)
    # else:
    #     db_sql.add_user(reg.user_id)
    #     sub_time = int(time.time()) + days_to_seconds(30)
    #     db_sql.set_sub_time(reg.user_id, sub_time)
    # await dp.bot.send_message(chat_id=reg.user_id, text="<b>⭐️ You've received a 1 month trial subscription to the bot.</b>")

@dp.callback_query_handler(text='decline_accept', chat_id=moderators)
async def accept_accept(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter ID to decline:')
    await decline_registration.user_id.set()

@dp.message_handler(state=decline_registration.user_id, chat_id=moderators)
async def accept_accept(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        user = await quick_commands.select_user(message.from_user.id)
        reg = await quick_commands.select_unregistered()
        user1 = await quick_commands.select_user(int(message.text))
        if user1:
            await quick_commands.delete_user_and_registration(int(message.text))
            await dp.bot.send_message(chat_id=reg.user_id, text='<b>🌐 Your registration has been <ins>declined</ins>.</b>\n\n')
            for moderator in moderators:
                await dp.bot.send_message(chat_id=moderator, text=f'<b>◀️ Registration of "<code>{reg.name}</code>" has been <ins>declined</ins> by the admin "{user.name}.</b>')
        else:
            await message.answer('⚠️ Wrong ID.')
    except AttributeError:
        await message.answer('⚠️ Wrong ID.')



