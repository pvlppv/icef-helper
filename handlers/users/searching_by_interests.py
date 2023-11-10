from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_search_by_interests import ikb_search_by_interests, \
    ikb_search_by_interests_specializations, ikb_search_by_interests_specializations_back, ikb_search_by_interests_back
from loader import dp
from utils.db_api import quick_commands

# search specialization
@dp.callback_query_handler(text='searching_by_interests')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Searching by interests:</b>', reply_markup=ikb_search_by_interests)

@dp.callback_query_handler(text='search_by_interests_back')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Searching by interests:</b>', reply_markup=ikb_search_by_interests)

@dp.callback_query_handler(text='search_by_interests_specializations_back')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Searching by <ins>specializations</ins>:</b>', reply_markup=ikb_search_by_interests_specializations)

@dp.callback_query_handler(text='search_by_specializations')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Searching by <ins>specializations</ins>:</b>', reply_markup=ikb_search_by_interests_specializations)

@dp.callback_query_handler(text='search_by_additional_courses')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Soon. Developing.</b>', reply_markup=ikb_search_by_interests_back)

@dp.callback_query_handler(text='search_by_sport')
async def command_search_interests(call: types.CallbackQuery):
    await call.message.edit_text('<b>🔎 Soon. Developing.</b>', reply_markup=ikb_search_by_interests_back)

@dp.callback_query_handler(text='bdf')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_bdf()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>🏦 Students with specialization "Банковское дело и финансы":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

@dp.callback_query_handler(text='emanage')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_emanage()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>💵 Students with specialization "Экономика и менеджмент":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

@dp.callback_query_handler(text='e')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_e()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>💴 Students with specialization "Экономика":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

@dp.callback_query_handler(text='ef')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_ef()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>💶 Students with specialization "Экономика и финансы":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

@dp.callback_query_handler(text='buf')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_buf()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>🗄 Students with specialization "Бухгалтерский учёт и финансы":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

@dp.callback_query_handler(text='emath')
async def command_search_interests(call: types.CallbackQuery):
    users = await quick_commands.select_profile_specialization_emath()
    _users1 = ''
    _users2 = ''
    _users3 = ''
    _users4 = ''
    for user in users:
        if user.course == 1:
            _users1 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 2:
            _users2 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 3:
            _users3 += f'<a href="{user.username}">{user.name}</a>\n'
        elif user.course == 4:
            _users4 += f'<a href="{user.username}">{user.name}</a>\n'
    await call.message.edit_text(f'<b>💷 Students with specialization "Экономика и математика":</b> <a href="https://telegra.ph/file/6429b89f9bc52dc8f2853.png">ㅤ</a>\n\n<b>1st course:</b>\n{_users1}\n<b>2nd course:</b>\n{_users2}\n<b>3rd course:</b>\n{_users3}\n<b>4th course:</b>\n{_users4}', reply_markup=ikb_search_by_interests_specializations_back)

