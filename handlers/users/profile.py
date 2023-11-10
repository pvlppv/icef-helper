import json
import traceback

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

from filters import IsPrivateMessage, IsDatabaseUserMessage, \
    IsSubscriptionUserAddedNoErrorPleaseMessage, IsAcceptedUserMessage, IsSubscriberChannelMessage
# from handlers.users.subscription import time_sub_day
from keyboards.default.keyboard_profile import kb_profile
from keyboards.inline.inline_keyboard_profile import ikb_profile, ikb_profile_back
from keyboards.inline.inline_keyboard_registration import ikb_registration
from loader import dp, db_sql
from states import checkprofile
from utils.db_api import quick_commands
from utils.misc import rate_limit

@rate_limit(limit=3, key='👤 Profile')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='👤 Profile')
async def command_profile(message: types.Message):
    await message.answer('<b>👤 Profile:</b>', reply_markup=ikb_profile)

@dp.callback_query_handler(text='profile_back')
async def command_profile_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>👤 Profile:</b>', reply_markup=ikb_profile)

@dp.callback_query_handler(text='my_profile')
async def command_myprofile(call: types.CallbackQuery):
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
        # sub = time_sub_day(db_sql.get_sub_time(message.from_user.id))
        # if sub == False:
        #     sub = 'Not purchased'
        profile = (f'<b>👤 Profile:</b>\n\n <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>'
                   f'<b>👤 Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
                   f'      <b>📧 Email:</b> {user.email}\n'
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
                                     f"      {hbold('🏆 Rating position:')} {item.get('place')}\n"
                                     f"      {hbold('🧷 Average score:')} {item.get('average')}\n"
                                     f"      {hbold('🔗 Minimum score:')} {item.get('min')}\n"
                                     f"      {hbold('📎 Percentile:')} {item.get('percentile')}\n"
                                     f"      {hbold('🖇 GPA:')} {item.get('gpa')}\n\n"
                                     # f'<b>⭐️ Subscription:</b> {sub}\n\n'
                                     f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}', reply_markup=markup)
                break
        else:
            # time_str = user.created_at
            # date_format_str = '%d.%m.%Y %H:%M'
            # given_time = datetime.strptime(str(time_str), str(date_format_str))
            # final_time = str(user.created_at(format('%d.%m.%Y %H:%M')) + timedelta(hours=3))
            # final_time_str = final_time.strftime('%d.%m.%Y %H:%M')
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
                             'Click the button below to register and enter to the bot. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>',
                             reply_markup=ikb_registration)
    except:
        print(traceback.format_exc())



@dp.callback_query_handler(text='another_profile')
async def command_anotherprofile(call: types.CallbackQuery):
    await call.message.edit_text(f'✏️ Enter "Имя Фамилия":')
    await checkprofile.answer.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=checkprofile.answer)
async def command_anotherprofile_answer(message: types.Message, state: FSMContext):
        try:

            # collect_data()

            markup = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='⬅️ Back', callback_data='profile_back')
                                              ]
                                          ])

            answer = message.text
            await state.update_data(text=answer)
            user = await quick_commands.select_user_name(answer)
            student = user.name
            if db_sql.user_exists(user.user_id):
                pass
            else:
                db_sql.add_user(user.user_id)
            # sub = time_sub_day(db_sql.get_sub_time(user.user_id))
            # if sub == False:
            #     sub = 'Not purchased'
            profile = (f'<b>👤 Profile:</b>\n\n <a href="https://telegra.ph/file/6854b1397c257a1391356.png">ㅤ</a>'
                       f'<b>👤 Name:</b> <ins><a href="{user.username}">{user.name}</a></ins>\n'
                       f'      <b>📧 Email:</b> {user.email}\n'
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
                    await message.answer(f"{profile}\n"
                                         f"      {hbold('🏆 Rating position:')} {item.get('place')}\n"
                                         f"      {hbold('🧷 Average score:')} {item.get('average')}\n"
                                         f"      {hbold('🔗 Minimum score:')} {item.get('min')}\n"
                                         f"      {hbold('📎 Percentile:')} {item.get('percentile')}\n"
                                         f"      {hbold('🖇 GPA:')} {item.get('gpa')}\n\n"
                                         # f'<b>⭐️ Subscription:</b> {sub}\n\n'
                                        f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}', reply_markup=markup)
                    break
            else:
                await message.answer(f'{profile}\n'
                                     f'      [Нет данных о рейтинге]\n'
                                     f'      <b>🏆 Rating position:</b> None\n'
                                     f'      <b>🧷 Average score:</b> None\n'
                                     f'      <b>🔗 Minimum score:</b> None\n'
                                     f'      <b>📎 Percentile:</b> None\n'
                                     f'      <b>🖇 GPA:</b> None\n\n'
                                     # f'<b>⭐️ Subscription:</b> {sub}\n\n'
                                     f'<b>📱 Registered:</b> {user.created_at.strftime(format="%d.%m.%Y %H:%M")}', reply_markup=markup)
        except AttributeError:
            await message.answer("⚠️ Student is not found.", reply_markup=ikb_profile_back)

        except:
            print(traceback.format_exc())

        await state.finish()

@rate_limit(limit=3, key='⬅️ Profile')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Profile')
async def command_profile_back(message: types.Message):
    await message.answer('<b>👤 Profile:</b>', reply_markup=kb_profile)