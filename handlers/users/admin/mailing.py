from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from filters import IsPrivateMessage
from keyboards.inline.inline_keyboard_settings import ikb_settings_admin_mailing
from loader import dp
from utils.db_api import quick_commands as commands
from states import mailing

from data.config import moderators

@dp.callback_query_handler(chat_id=moderators, text='mailing0')
async def edit_timetable_command(call: types.CallbackQuery):
    await call.message.edit_text('<b>✏️ Mailing:</b>', reply_markup=ikb_settings_admin_mailing)

@dp.callback_query_handler(text='mailing', chat_id=moderators)
async def start_mailing(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Enter text for mailing:')
    await mailing.text.set()

@dp.message_handler(IsPrivateMessage(), state=mailing.text, chat_id=moderators)
async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Add photo', callback_data='add_photo'),
                                          InlineKeyboardButton(text='✅ Send mailing', callback_data='send_mailing_text'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel')
                                      ]
                                  ])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await mailing.state.set()

@dp.callback_query_handler(text='send_mailing_text', state=mailing.state, chat_id=moderators)
async def start(call: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users()
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            print(f'Mailing went to:\n'
                  f'{user}')
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await dp.bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('<b>🔤 Mailing <ins>has been sent</ins> to everyone.</b>')

@dp.callback_query_handler(text='add_photo', state=mailing.state, chat_id=moderators)
async def add_photo(call: types.CallbackQuery):
    await call.message.answer('✏️ Send a photo for mailing:')
    await mailing.photo.set()


@dp.message_handler(IsPrivateMessage(), state=mailing.photo, content_types=types.ContentTypes.PHOTO, chat_id=moderators)
async def mailing_text(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='✅ Send mailing', callback_data='send_mailing_photo'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel')
                                      ]
                                  ])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)


@dp.callback_query_handler(text='send_mailing_photo', state=mailing.photo, chat_id=moderators)
async def start(call: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users()
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            print(f'Mailing went to:\n'
                  f'{user}')
            try:
                await dp.bot.send_photo(chat_id=user.user_id, photo=photo, caption=text)
                await sleep(0.33)
            except Exception:
                pass
        else:
            pass
    await dp.bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('<b>🔤 Mailing <ins>has been sent</ins> to everyone.</b>')


@dp.message_handler(IsPrivateMessage(), state=mailing.photo, chat_id=moderators)
async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel')
                                      ]
                                  ])
    await message.answer('✏️ Send a photo for mailing:', reply_markup=markup)


@dp.callback_query_handler(text='cancel', state=[mailing.text, mailing.photo, mailing.state], chat_id=moderators)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await dp.bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('<b>✏️ Mailing <ins>has been canceled</ins>.</b>')








