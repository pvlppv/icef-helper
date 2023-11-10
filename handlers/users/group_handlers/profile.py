import json

import traceback

from aiogram import types

from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from loader import dp
from utils.db_api import quick_commands
from utils.misc import rate_limit
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
# from handlers.users.rating_main_parsing import collect_data
from aiogram.utils.markdown import hbold



@rate_limit(limit=3, key='/profile')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/profile')
async def profile(message: types.Message):
    try:

        # collect_data()

        user = await quick_commands.select_user(message.from_user.id)
        student = user.name
        profile = (f'<b>👤 Profile</b>\n\n'
                   f'<b>👤 Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
                   f'<b>      👥 Course:</b> {user.course}\n'
                   f'      <b>🫂 Academic group:</b> {user.academic_group}\n'
                   f'      <b>🇬🇧 English group:</b> {user.english_group}\n'
                   f'<b>      💼 Specialization:</b> {user.specialization}\n'
                   f'<b>      🔭 Additional courses:</b> {user.additional_courses}\n'
                   f'<b>      🎱 Sport:</b> {user.sport}')

        # with open('/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/result_data.json') as file:
        with open("/root/bot/handlers/users/result_data.json") as file:
            data = json.load(file)

        for item in data:
            if item["name"] == student:
                await message.answer(f"{profile}\n"
                                     f"      {hbold('🏆 Rating position:')} {item.get('place')}\n" \
                                     f"      {hbold('🧷 Average score:')} {item.get('average')}\n" \
                                     f"      {hbold('🔗 Minimum score:')} {item.get('min')}\n" \
                                     f"      {hbold('📎 Percentile:')} {item.get('percentile')}\n" \
                                     f"      {hbold('🖇 GPA:')} {item.get('gpa')}\n\n" \
                                     f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}')
                break
        else:
            await message.answer(f'{profile}\n'
                                 f'      [Нет данных о рейтинге]\n'
                                 f'      <b>🏆 Rating position:</b> None\n'
                                 f'      <b>🧷 Average score:</b> None\n'
                                 f'      <b>🔗 Minimum score:</b> None\n'
                                 f'      <b>📎 Percentile:</b> None\n'
                                 f'      <b>🖇 GPA:</b> None\n\n'
                                 f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}')
    except AttributeError:
        await message.answer("⚠️ Error.\n\n"
                             "Contact with @paoloppv.")
    except:
        print(traceback.format_exc())


@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/checkprofile')
async def command_checkprofile_1(message: types.Message):
    await message.answer('⚠️ /checkprofile Имя Фамилия')

@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), Command('checkprofile'))
async def command_checkprofile_2(message: Message):
    try:
        collect_data()

        answer = message.text[14:]

        user = await quick_commands.select_user_name(answer)
        student = user.name
        profile = (f'<b>👤 Profile</b>\n\n'
                   f'<b>👤 Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
                   f'      <b>👥 Course:</b> {user.course}\n'
                   f'      <b>🫂 Academic group:</b> {user.academic_group}\n'
                   f'      <b>🇬🇧 English group:</b> {user.english_group}\n'
                   f'      <b>💼 Specialization:</b> {user.specialization}\n'
                   f'      <b>🔭 Additional courses:</b> {user.additional_courses}\n'
                   f'      <b>🎱 Sport:</b> {user.sport}')

        # with open('/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/result_data.json') as file:
        with open("/root/bot/handlers/users/result_data.json") as file:
            data = json.load(file)

        for item in data:
            if item["name"] == student:
                await message.answer(f"{profile}\n"
                                     f"      {hbold('🏆 Rating position:')} {item.get('place')}\n" \
                                     f"      {hbold('🧷 Average score:')} {item.get('average')}\n" \
                                     f"      {hbold('🔗 Minimum score:')} {item.get('min')}\n" \
                                     f"      {hbold('📎 Percentile:')} {item.get('percentile')}\n" \
                                     f"      {hbold('🖇 GPA:')} {item.get('gpa')}\n\n" \
                                     f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}')
                break
        else:
            await message.answer(f'{profile}\n'
                                 f'      [Нет данных о рейтинге]\n'
                                 f'      <b>🏆 Rating position:</b> None\n'
                                 f'      <b>🧷 Average score:</b> None\n'
                                 f'      <b>🔗 Minimum score:</b> None\n'
                                 f'      <b>📎 Percentile:</b> None\n'
                                 f'      <b>🖇 GPA:</b> None\n\n'
                                 f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}')
    except AttributeError:
        await message.answer("⚠️ Student is not found.")

    except:
        print(traceback.format_exc())

