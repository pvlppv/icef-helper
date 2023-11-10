# from asyncio import sleep
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# from data.config import moderators
# from filters import IsPrivateMessage
# from keyboards.inline.inline_keyboard_settings import ikb_settings_admins_subjects
# from keyboards.inline.inline_keyboard_subjects_professors import ikb_subjects_professors
# from loader import dp
# from states import changeicefevents
# from states.editprofessors import edit_calculus_professors, edit_statistics_professors, edit_microeconomics_professors, \
#     edit_macroeconomics_professors, edit_history_professors, edit_philosophy_professors, edit_ics_professors
#
#
# @dp.callback_query_handler(text='edit_subjects_professors')
# async def admin_panel_back(call: types.CallbackQuery):
#     await call.message.edit_text(f'<b>📚 Editing of subjects - <ins>professors</ins>:</b>', reply_markup=ikb_subjects_professors)
#
# # calculus
# @dp.callback_query_handler(text='edit_calculus_professors', chat_id=moderators)
# async def start_edit_calculus_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of calculus professors:')
#     await edit_calculus_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_calculus_professors.text, chat_id=moderators)
# async def edit_calculus_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_calculus_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_calculus_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_calculus_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_calculus_professors_change', state=edit_calculus_professors.text, chat_id=moderators)
# async def change_edit_calculus_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("calculus_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📘 List of calculus professors <ins>has been changed</ins>.</b>')
#     f = open("calculus_professors.txt", "r")
#     calculus_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📘 Calculus professors:</b>\n\n'
#                          f'{calculus_professors}')
#
# @dp.callback_query_handler(text='edit_calculus_professors_rechange', state=edit_calculus_professors.text, chat_id=moderators)
# async def rechange_edit_calculus_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of calculus professors:')
#     await edit_calculus_professors.text.set()
#
# @dp.callback_query_handler(text='edit_calculus_professors_cancel', state=[edit_calculus_professors.text], chat_id=moderators)
# async def cancel_edit_calculus_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📘 List of calculus professors <ins>hasn't been changed</ins>.</b>")
#
# # statistics
# @dp.callback_query_handler(text='edit_statistics_professors', chat_id=moderators)
# async def start_edit_statistics_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of statistics professors:')
#     await edit_statistics_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_statistics_professors.text, chat_id=moderators)
# async def edit_statistics_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_statistics_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_statistics_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_statistics_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_statistics_professors_change', state=edit_statistics_professors.text, chat_id=moderators)
# async def change_edit_statistics_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("statistics_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📗 List of statistics professors <ins>has been changed</ins>.</b>')
#     f = open("statistics_professors.txt", "r")
#     statistics_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📗 Statistics professors:</b>\n\n'
#                          f'{statistics_professors}')
#
# @dp.callback_query_handler(text='edit_statistics_professors_rechange', state=edit_statistics_professors.text, chat_id=moderators)
# async def rechange_edit_statistics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of statistics professors:')
#     await edit_statistics_professors.text.set()
#
# @dp.callback_query_handler(text='edit_statistics_professors_cancel', state=[edit_statistics_professors.text], chat_id=moderators)
# async def cancel_edit_statistics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📗 List of statistics professors <ins>hasn't been changed</ins>.</b>")
#
# # microeconomics
# @dp.callback_query_handler(text='edit_microeconomics_professors', chat_id=moderators)
# async def start_edit_microeconomics_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of microeconomics professors:')
#     await edit_microeconomics_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_microeconomics_professors.text, chat_id=moderators)
# async def edit_microeconomics_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_microeconomics_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_microeconomics_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_microeconomics_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_microeconomics_professors_change', state=edit_microeconomics_professors.text, chat_id=moderators)
# async def change_edit_microeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("microeconomics_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📙 List of microeconomics professors <ins>has been changed</ins>.</b>')
#     f = open("microeconomics_professors.txt", "r")
#     microeconomics_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📙 Microeconomics professors:</b>\n\n'
#                          f'{microeconomics_professors}')
#
# @dp.callback_query_handler(text='edit_microeconomics_professors_rechange', state=edit_microeconomics_professors.text, chat_id=moderators)
# async def rechange_edit_microeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of microeconomics professors:')
#     await edit_microeconomics_professors.text.set()
#
# @dp.callback_query_handler(text='edit_microeconomics_professors_cancel', state=[edit_microeconomics_professors.text], chat_id=moderators)
# async def cancel_edit_microeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📙 List of microeconomics professors <ins>hasn't been changed</ins>.</b>")
#
# # macroeconomics
# @dp.callback_query_handler(text='edit_macroeconomics_professors', chat_id=moderators)
# async def start_edit_macroeconomics_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of macroeconomics professors:')
#     await edit_macroeconomics_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_macroeconomics_professors.text, chat_id=moderators)
# async def edit_macroeconomics_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_macroeconomics_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_macroeconomics_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_macroeconomics_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_macroeconomics_professors_change', state=edit_macroeconomics_professors.text, chat_id=moderators)
# async def change_edit_macroeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("macroeconomics_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📕 List of macroeconomics professors <ins>has been changed</ins>.</b>')
#     f = open("macroeconomics_professors.txt", "r")
#     macroeconomics_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📕 macroeconomics professors:</b>\n\n'
#                          f'{macroeconomics_professors}')
#
# @dp.callback_query_handler(text='edit_macroeconomics_professors_rechange', state=edit_macroeconomics_professors.text, chat_id=moderators)
# async def rechange_edit_macroeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of macroeconomics professors:')
#     await edit_macroeconomics_professors.text.set()
#
# @dp.callback_query_handler(text='edit_macroeconomics_professors_cancel', state=[edit_macroeconomics_professors.text], chat_id=moderators)
# async def cancel_edit_macroeconomics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📕 List of macroeconomics professors <ins>hasn't been changed</ins>.</b>")
#
# # history
# @dp.callback_query_handler(text='edit_history_professors', chat_id=moderators)
# async def start_edit_history_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of history professors:')
#     await edit_history_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_history_professors.text, chat_id=moderators)
# async def edit_history_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_history_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_history_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_history_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_history_professors_change', state=edit_history_professors.text, chat_id=moderators)
# async def change_edit_history_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("history_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📔 List of history professors <ins>has been changed</ins>.</b>')
#     f = open("history_professors.txt", "r")
#     history_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📔 History professors:</b>\n\n'
#                          f'{history_professors}')
#
# @dp.callback_query_handler(text='edit_history_professors_rechange', state=edit_history_professors.text, chat_id=moderators)
# async def rechange_edit_history_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of history professors:')
#     await edit_history_professors.text.set()
#
# @dp.callback_query_handler(text='edit_history_professors_cancel', state=[edit_history_professors.text], chat_id=moderators)
# async def cancel_edit_history_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📔 List of history professors <ins>hasn't been changed</ins>.</b>")
#
# # philosophy
# @dp.callback_query_handler(text='edit_philosophy_professors', chat_id=moderators)
# async def start_edit_philosophy_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of philosophy professors:')
#     await edit_philosophy_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_philosophy_professors.text, chat_id=moderators)
# async def edit_philosophy_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_philosophy_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_philosophy_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_philosophy_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_philosophy_professors_change', state=edit_philosophy_professors.text, chat_id=moderators)
# async def change_edit_philosophy_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("philosophy_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📒 List of philosophy professors <ins>has been changed</ins>.</b>')
#     f = open("philosophy_professors.txt", "r")
#     philosophy_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📒 Philosophy professors:</b>\n\n'
#                          f'{philosophy_professors}')
#
# @dp.callback_query_handler(text='edit_philosophy_professors_rechange', state=edit_philosophy_professors.text, chat_id=moderators)
# async def rechange_edit_philosophy_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of philosophy professors:')
#     await edit_philosophy_professors.text.set()
#
# @dp.callback_query_handler(text='edit_philosophy_professors_cancel', state=[edit_philosophy_professors.text], chat_id=moderators)
# async def cancel_edit_philosophy_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📒 List of philosophy professors <ins>hasn't been changed</ins>.</b>")
#
# # ics
# @dp.callback_query_handler(text='edit_ics_professors', chat_id=moderators)
# async def start_edit_ics_professors(call: types.CallbackQuery):
#     await call.message.answer(f'✏️ Send a new list of ICS professors:')
#     await edit_ics_professors.text.set()
#
# @dp.message_handler(IsPrivateMessage(), state=edit_ics_professors.text, chat_id=moderators)
# async def edit_ics_professors_text(message: types.Message, state: FSMContext):
#     answer = message.text
#     markup = InlineKeyboardMarkup(row_width=2,
#                                   inline_keyboard=[
#                                       [
#                                           InlineKeyboardButton(text='✅ Change', callback_data='edit_ics_professors_change'),
#                                           InlineKeyboardButton(text='🔄 Rechange', callback_data='edit_ics_professors_rechange'),
#                                           InlineKeyboardButton(text='❌ Cancel', callback_data='edit_ics_professors_cancel'),
#                                       ]
#                                   ])
#     await state.update_data(text=answer)
#     await message.answer(text=answer, reply_markup=markup)
#
# @dp.callback_query_handler(text='edit_ics_professors_change', state=edit_ics_professors.text, chat_id=moderators)
# async def change_edit_ics_professors(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     list = data.get('text')
#     with open("ics_professors.txt", "w") as file:
#         file.write(list)
#     await state.finish()
#     await call.message.edit_text('<b>📓 List of ICS professors <ins>has been changed</ins>.</b>')
#     f = open("ics_professors.txt", "r")
#     ics_professors = f.read()
#     f.close()
#     await call.message.answer(f'<b>📓 ICS professors:</b>\n\n'
#                          f'{ics_professors}')
#
# @dp.callback_query_handler(text='edit_ics_professors_rechange', state=edit_ics_professors.text, chat_id=moderators)
# async def rechange_edit_ics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.answer(f'✏️ Send a new list of ICS professors:')
#     await edit_ics_professors.text.set()
#
# @dp.callback_query_handler(text='edit_ics_professors_cancel', state=[edit_ics_professors.text], chat_id=moderators)
# async def cancel_edit_ics_professors(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text("<b>📓 List of ICS professors <ins>hasn't been changed</ins>.</b>")
