# from aiogram import types
# from aiogram.dispatcher import FSMContext
# import os
#
# from data.config import moderators
# from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
#     IsSubscriberChannelMessage
# from keyboards.inline.inline_keyboard_settings import ikb_settings_admins, ikb_files_timetable, \
#     ikb_files_notification_timetable
# from loader import dp
# from states.files import edit_timetable
#
# from utils.db_api import quick_commands
# from utils.misc import rate_limit
#
#
# @dp.callback_query_handler(chat_id=moderators, text='edit_timetable')
# async def edit_timetable_command(call: types.CallbackQuery):
#     await call.message.edit_text('<b>🔔 Editing of timetable:</b>', reply_markup=ikb_files_timetable)
#
# @dp.callback_query_handler(chat_id=moderators, text='timetable_back')
# async def timetable_back(call: types.CallbackQuery):
#     await call.message.edit_text('<b>👨🏼‍💻 Admin Panel:</b>', reply_markup=ikb_settings_admins)
#
# @dp.callback_query_handler(chat_id=moderators, text='timetable_change')
# async def delete_previous_timetable(call: types.CallbackQuery, state: FSMContext):
#     await call.message.answer('<b>➖ Delete a previous timetable, enter its file name:</b>')
#     path = '/root/bot/media/Timetable'
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#     await edit_timetable.file_to_delete.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=edit_timetable.file_to_delete)
# async def edittimetable(message: types.Message, state: FSMContext):
#     answer = message.text
#     try:
#         path = f'/root/bot/media/Timetable/{answer}'
#         os.remove(path)
#     except FileNotFoundError:
#         pass
#     await message.answer('<b>➕ Send a new timetable:</b>')
#     await edit_timetable.file_file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=edit_timetable.file_file)
# async def edittimetable_state_file_name(message: types.Message, state: FSMContext):
#     document = message.document
#     await state.update_data(document=document)
#     await message.answer('<b>➕ Enter a new file name for the new timetable:</b>\n\n'
#                          '<em>Example: Timetable for 10.10-15.10</em>')
#     await edit_timetable.file_name.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=edit_timetable.file_name)
# async def edittimetable_state_file_name_0(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(file_name=answer)
#     data = await state.get_data()
#     document = data.get('document')
#     if document := document:
#         await document.download(
#             destination_file=f'media/Timetable/{answer}.pdf'
#         )
#         await message.answer(f'<b>➕ Timetable <ins>has been changed</ins>.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_timetable)
#
# @dp.callback_query_handler(text='send_notification_timetable', chat_id=moderators, state=edit_timetable.file_name)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>🔔 Timetable has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}.pdf'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_timetable)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=edit_timetable.file_name)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await state.finish()
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_timetable)
#
# @rate_limit(limit=3, key='🔔 Timetable')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🔔 Timetable')
# async def timetable(message: types.Message, state: FSMContext):
#     # pdf_bytes = InputFile(path_or_bytesio='media/Timetable 12.09-24.09.pdf')
#
#     # await dp.bot.send_document(chat_id=chat_id, document=pdf_bytes, caption='<b>🔔 Timetable for 12.09-24.09</b>')
#
#     chat_id = message.from_user.id
#     await message.answer('<b>🔔 Timetable:</b>')
#     path = '/root/bot/media/Timetable'
#     files = []
#     # r = root, d = directories, f = files
#     for r, d, f in os.walk(path):
#         for file in f:
#             files.append(os.path.join(r, file))
#     for f in files:
#         await dp.bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
#
