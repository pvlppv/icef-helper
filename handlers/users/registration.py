import traceback

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.json import json
from aiogram.utils.markdown import hbold

from data.config import admins, admin, moderators
from filters import IsPrivateMessage
# from handlers.users.rating_main_parsing import collect_data
# from handlers.users.subscription import time_sub_day
from keyboards.default import kb_profile
from keyboards.default.keyboard_skipregistration import kb_skipregistration
from keyboards.inline.inline_keyboard_registration import ikb_registration
from keyboards.inline.inline_keyboard_settings import ikb_settings_admins_edit_registrations
from loader import dp, db_sql, bot
from states import registration
from utils.db_api import quick_commands
import ruz.utils


@dp.message_handler(IsPrivateMessage(), Command('start'))
async def command_start_to_register(message: types.Message):
    user = await quick_commands.select_user(message.from_user.id)
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='👤 My profile', callback_data='myprofile'),
                                      ]
                                  ])
    if user:
        if user.status == 'Accepted':
            await message.answer("<b>🌐 You've already registered.</b>\n\n"
                                 'Click the button below to check your profile. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=markup)
        else:
            await message.answer("<b>🌐 Your registration is still on a check.</b>\n\n")
    # else:
    #     await message.answer('<b>🌐 Welcome to <ins>ICEF Helper</ins>.</b>\n\n'
    #                          "⚠️ It's private - only for ICEF students. To get an access, contact with @paoloppv.")
    else:
        await message.answer(f'<b>🌐 Welcome to <ins>ICEF Helper</ins>.</b>\n\n'
                             f'Click the button below to register and enter to the bot. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>',
                             reply_markup=ikb_registration)
        # if status:
        #     await message.answer("<b>🌐 You've already registered.</b>\n\n"
        #                      "Click the button below to check your profile.", reply_markup=markup)
        # else:
        #     await message.answer("<b>🌐 Your registration is still checking by admins.</b>")




@dp.callback_query_handler(text='register')
async def command_reg(call: types.CallbackQuery):
    await call.message.answer(f"<b>🌐 You've started registration.</b>")
    await call.message.answer(f'1. Enter your name (Имя Фамилия):\n\n'
                              f'<em>Example: Алла Фридман</em>'
                              )
    await registration.name.set()

@dp.message_handler(IsPrivateMessage(), state=registration.name)
async def command_get_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        await message.answer('⚠️ Enter correct name.')
    else:
        await state.update_data(user_id=message.from_user.id)
        await state.update_data(username=message.from_user.username)
        await state.update_data(name=answer)
        await message.answer('2. Enter your HSE email (email@edu.hse.ru):')
        await registration.email.set()

@dp.message_handler(IsPrivateMessage(), state=registration.email)
async def command_get_email(message: types.Message, state: FSMContext):
    answer = message.text
    is_hse_email = ruz.utils.is_hse_email(email=answer)
    is_valid_hse_email = ruz.utils.is_valid_hse_email(email=answer)
    if is_hse_email + is_valid_hse_email:
        await state.update_data(email=answer)
        await message.answer('3. Enter your course number (1-4):')
        await registration.course.set()
    else:
        await message.answer('⚠️ Enter correct HSE email.')

@dp.message_handler(IsPrivateMessage(), state=registration.course)
async def command_get_course(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        if int(answer) < 5:
            if int(answer) > 0:
                await state.update_data(course=int(answer))
                await message.answer('4. Enter your academic group number (1-11):')
                await registration.academic_group.set()
            else:
                await message.answer('⚠️ Enter correct course number.')
        else:
            await message.answer('⚠️ Enter correct course number.')
    else:
        await message.answer('⚠️ Enter correct course number.')

@dp.message_handler(IsPrivateMessage(), state=registration.academic_group)
async def command_get_academicgroup(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        if int(answer) < 12:
            if int(answer) > 0:
                await state.update_data(academic_group=int(answer))
                await message.answer(f'5. Enter your specialization:\n\n'
                                     f'<em>Example: Экономика и финансы</em>\n\n'
                                     f'🏦 Банковское дело и финансы\n'
                                     f'💵 Экономика и менеджмент\n'
                                     f'💴 Экономика\n'
                                     f'💶 Экономика и финансы\n'
                                     f'🗄 Бухгалтерский учёт и финансы\n'
                                     f'💷 Экономика и математика'
                                     , reply_markup=kb_skipregistration)
                await registration.specialization.set()
            else:
                await message.answer('⚠️ Enter correct academic group number.')
        else:
            await message.answer('⚠️ Enter correct academic group number.')
    else:
        await message.answer('⚠️ Enter correct academic group number.')

@dp.message_handler(IsPrivateMessage(), state=registration.specialization)
async def command_get_specialization(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '💨 Skip':
        await message.answer(f'6. Enter your additional courses:\n\n'
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
                             f'🧘 Yoga\n'
                             f'- etc.'
                             , reply_markup=kb_skipregistration)
        await registration.additional_cources.set()
    else:
        if answer.isnumeric():
            await message.answer('⚠️ Enter correct specialization.')
        else:
            await state.update_data(specialization=answer)
            await message.answer(f'6. Enter your additional courses:\n\n'
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
                                 f'🧘 Yoga\n'
                                 f'- etc.'
                                 , reply_markup=kb_skipregistration)
            await registration.additional_cources.set()

@dp.message_handler(IsPrivateMessage(), state=registration.additional_cources)
async def command_get_additionalcourses(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '💨 Skip':
        await message.answer(f'7. Enter your sport:\n\n'
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
                             , reply_markup=kb_skipregistration)
        await registration.sport.set()
    else:
        if answer.isnumeric():
            await message.answer('⚠️ Enter correct additional courses.')
        else:
            await state.update_data(additional_courses=answer)
            await message.answer(f'7. Enter your sport:\n\n'
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
                                 , reply_markup=kb_skipregistration)
            await registration.sport.set()

@dp.message_handler(IsPrivateMessage(), state=registration.sport)
async def command_get_sport(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '💨 Skip':
        data = await state.get_data()
        user_id = data.get('user_id')
        username = f'https://t.me/' + data.get('username')
        name = data.get('name')
        course = data.get('course')
        academic_group = data.get('academic_group')
        specialization = data.get('specialization')
        additional_courses = data.get('additional_courses')
        sport = data.get('sport')
        email = data.get('email')
        await quick_commands.new_user(user_id=user_id,
                                      name=name,
                                      username=username,
                                      course=course,
                                      academic_group=academic_group,
                                      specialization=specialization,
                                      additional_courses=additional_courses,
                                      sport=sport,
                                      email=email,
                                      status='None')
        await message.answer(f"<b>🌐 Your registration has been sent to the admins for a check.</b>\n\n")
        await state.finish()

        for moderator in moderators:
            await dp.bot.send_message(chat_id=moderator, text=f'<b>🌐 New registration from "<code>{name}</code>".</b>',
                                      reply_markup=ikb_settings_admins_edit_registrations)
    else:
        if answer.isnumeric():
            await message.answer('⚠️ Enter correct sport.')
        else:
            await state.update_data(sport=answer)
            data = await state.get_data()
            user_id = data.get('user_id')
            username = f'https://t.me/' + data.get('username')
            name = data.get('name')
            course = data.get('course')
            academic_group = data.get('academic_group')
            specialization = data.get('specialization')
            additional_courses = data.get('additional_courses')
            sport = data.get('sport')
            email = data.get('email')
            await quick_commands.new_user(user_id=user_id,
                                          name=name,
                                          username=username,
                                          course=course,
                                          academic_group=academic_group,
                                          specialization=specialization,
                                          additional_courses=additional_courses,
                                          sport=sport,
                                          email=email,
                                          status='None')
            await message.answer(f"<b>🌐 Your registration has been sent to the admins for a check.</b>\n\n")
            await state.finish()

            for moderator in moderators:
                await dp.bot.send_message(chat_id=moderator, text=f'<b>🌐 New registration from "<code>{name}</code>".</b>', reply_markup=ikb_settings_admins_edit_registrations)
        # await message.answer(f"<b>🌐 You've successfully registered.</b>\n\n"
        #                      f"Communication with the bot is only with the menu below.", reply_markup=kb_menu)
        # await message.answer(f'⭐️ Full access to the bot is only with the subscription.\n\n'
        #                      f'Click the button below to get more information.', reply_markup=ikb_start)


@dp.callback_query_handler(text='myprofile')
async def command_reg_profile(call: types.CallbackQuery):
    try:

        # collect_data()

        markup = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='✏️ Edit profile', callback_data='editprofile'),
                                          ]
                                      ])
        user = await quick_commands.select_user(call.from_user.id)
        student = user.name
        # sub = time_sub_day(db_sql.get_sub_time(call.from_user.id))
        # if sub == False:
        #     sub = 'None'
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







