from aiogram import types
from keyboards.inline.inline_keyboard_settings import ikb_settings_admins_back, ikb_settings_all_users, \
    ikb_settings_all_users_back
from loader import dp
from utils.db_api import quick_commands



@dp.callback_query_handler(text='all_users')
async def command_all_users(call: types.CallbackQuery):
    await call.message.edit_text('<b>👤 All users:</b>', reply_markup=ikb_settings_all_users)

@dp.callback_query_handler(text='all_users_back')
async def command_all_users(call: types.CallbackQuery):
    await call.message.edit_text('<b>👤 All users:</b>', reply_markup=ikb_settings_all_users)

#     users = await quick_commands.select_all_users()
#     _users1 = ''
#     _users2 = ''
#     _users3 = ''
#     _users4 = ''
#     for user in users:
#         if user.course == 1:
#             _users1 += f'<a href="{user.username}">{user.name}</a>\n'
#         elif user.course == 2:
#             _users2 += f'<a href="{user.username}">{user.name}</a>\n'
#         elif user.course == 3:
#             _users3 += f'<a href="{user.username}">{user.name}</a>\n'
#         elif user.course == 4:
#             _users4 += f'<a href="{user.username}">{user.name}</a>\n'
#     await call.message.edit_text(f'<b>👤 All users:</b>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_settings_admins_back)

@dp.callback_query_handler(text='all_users_1')
async def command_all_users_1(call: types.CallbackQuery):
    users = await quick_commands.select_all_users()
    users1 = await quick_commands.count_users_1course()
    _users1 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'👤 1st course users: <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>\n\n{_users1}\nTotal: {users1}', reply_markup=ikb_settings_all_users_back)

@dp.callback_query_handler(text='all_users_2')
async def command_all_users_2(call: types.CallbackQuery):
    users = await quick_commands.select_all_users()
    users1 = await quick_commands.count_users_2course()
    _users2 = ''
    for user in users:
        if user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'👤 2nd course users: <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>\n\n{_users2}\nTotal: {users1}', reply_markup=ikb_settings_all_users_back)

@dp.callback_query_handler(text='all_users_3')
async def command_all_users_3(call: types.CallbackQuery):
    users = await quick_commands.select_all_users()
    users1 = await quick_commands.count_users_3course()
    _users3 = ''
    for user in users:
        if user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'👤 3rd course users: <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>\n\n{_users3}\nTotal: {users1}', reply_markup=ikb_settings_all_users_back)

@dp.callback_query_handler(text='all_users_4')
async def command_all_users_4(call: types.CallbackQuery):
    users = await quick_commands.select_all_users()
    users1 = await quick_commands.count_users_4course()
    _users4 = ''
    for user in users:
        if user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'👤 4th course users: <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>\n\n{_users4}\nTotal: {users1}', reply_markup=ikb_settings_all_users_back)


