from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import moderators
from filters import IsPrivateMessage
from keyboards.inline.inline_keyboard_settings import ikb_settings_admin_edit_events
from loader import dp
from states import changeicefevents

@dp.callback_query_handler(chat_id=moderators, text='edit_events0')
async def edit_timetable_command(call: types.CallbackQuery):
    await call.message.edit_text('<b>🎫 Editing of ICEF events:</b>', reply_markup=ikb_settings_admin_edit_events)

@dp.callback_query_handler(text='edit_events', chat_id=moderators)
async def start_changeicefevents(call: types.CallbackQuery):
    await call.message.answer(f'✏️ Send a new list of events:\n\n'
                         f'<em>Example:</em>\n'
                         f'<code>📍 Posvyat by @ICEFcrew\n'
                         f'Date: 10.09\n'
                         f'Time: 18:00\n'
                         f'Address: Pokrovsky Bulvar, 11</code>')
    await changeicefevents.text.set()

@dp.message_handler(IsPrivateMessage(), state=changeicefevents.text, chat_id=moderators)
async def changeicefevents_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='✅ Change', callback_data='change'),
                                          InlineKeyboardButton(text='🔄 Rechange', callback_data='rechange'),
                                          InlineKeyboardButton(text='❌ Cancel', callback_data='cancel'),
                                      ]
                                  ])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)


# кнопочка next
@dp.callback_query_handler(text='change', state=changeicefevents.text, chat_id=moderators)
async def change_changeicefevents(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    list = data.get('text')
    with open("root/bot/icef_events.txt", "w") as file:
        file.write(list)
    await state.finish()
    await call.message.edit_text('<b>🎫 List of events <ins>has been changed</ins>.</b>')
    f = open("root./bot/icef_events.txt", "r")
    icef_events = f.read()
    f.close()
    await call.message.answer(f'<b>🎫 ICEF events:</b>\n\n <a href="https://telegra.ph/file/a5a0f32790645d24af63d.png">ㅤ</a>'
                         f'{icef_events}')
# кнопочка rechange
@dp.callback_query_handler(text='rechange', state=changeicefevents.text, chat_id=moderators)
async def rechange_changeicefevents(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(f'✏️ Send a new list of events:')
    await changeicefevents.text.set()


# кнопочка cancel
@dp.callback_query_handler(text='cancel', state=[changeicefevents.text], chat_id=moderators)
async def cancel_changeicefevents(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("<b>🎫 List of events <ins>hasn't been changed</ins>.</b>")
