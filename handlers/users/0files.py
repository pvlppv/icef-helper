# import os
# import shutil
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from data.config import moderators
# from filters import IsPrivateMessage
# from keyboards.inline.inline_keyboard_files_subjects import ikb_files_statistics, ikb_files_microeconomics, \
#     ikb_files_english, ikb_files_ics, ikb_delete_files_subjects, ikb_delete_files_calculus, ikb_delete_files_statistics, \
#     ikb_files_macroeconomics, ikb_delete_files_microeconomics, \
#     ikb_files_notification_calculus_classes, ikb_files_notification_calculus_homework, \
#     ikb_files_notification_calculus_books, ikb_delete_files_macroeconomics, ikb_delete_files_english, \
#     ikb_delete_files_ics, ikb_files_notification_statistics_classes, ikb_files_notification_statistics_homework, \
#     ikb_files_notification_statistics_books, ikb_files_notification_microeconomics_classes, \
#     ikb_files_notification_microeconomics_homework, ikb_files_notification_microeconomics_books, \
#     ikb_files_notification_macroeconomics_classes, ikb_files_notification_macroeconomics_homework, \
#     ikb_files_notification_macroeconomics_books, ikb_files_notification_english_books, \
#     ikb_files_notification_english_homework, ikb_files_notification_english_classes, ikb_files_notification_ics_books, \
#     ikb_files_notification_ics_homework, ikb_files_notification_ics_classes, ikb_delete_files_history, \
#     ikb_delete_files_philosophy, ikb_files_history, ikb_files_notification_history_books, \
#     ikb_files_notification_history_homework, ikb_files_notification_history_classes, ikb_files_philosophy, \
#     ikb_files_notification_philosophy_books, ikb_files_notification_philosophy_homework, \
#     ikb_files_notification_philosophy_classes, ikb_files_subjects, ikb_files_calculus, ikb_files_manager
# from loader import dp
# from states.files import delete_calculus_classes, delete_calculus_homework, delete_calculus_books, \
#     delete_statistics_books, delete_statistics_homework, delete_statistics_classes, delete_microeconomics_books, \
#     delete_microeconomics_homework, delete_microeconomics_classes, delete_macroeconomics_books, \
#     delete_macroeconomics_homework, delete_macroeconomics_classes, delete_english_books, delete_english_homework, \
#     delete_english_classes, delete_ics_books, delete_ics_homework, delete_ics_classes, delete_history_books, \
#     delete_history_homework, delete_history_classes, delete_philosophy_books, delete_philosophy_homework, \
#     delete_philosophy_classes, calculus_classes, calculus_homework, calculus_books, statistics_classes, statistics_homework, \
#     statistics_books, microeconomics_books, microeconomics_homework, microeconomics_classes, english_homework, \
#     english_books, english_classes, ics_books, ics_homework, ics_classes, macroeconomics_books, macroeconomics_classes, \
#     macroeconomics_homework, history_books, history_homework, history_classes, philosophy_books, philosophy_homework, \
#     philosophy_classes
#
# # files manager
# from utils.db_api import quick_commands
#
#
# @dp.message_handler(IsPrivateMessage(), text='/files', chat_id=moderators)
# async def files_manager_command(message: types.Message):
#     await message.answer('<b>🗂 Manager of the files:</b>'
#                          , reply_markup=ikb_files_manager)
#
# @dp.callback_query_handler(text='files_cancel', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>❌ Manager of the files is closed.</b>')
#
#
# # ------------------ delete files
# @dp.callback_query_handler(text='delete_files', chat_id=moderators)
# async def delete_files_command(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_subjects)
#
# # delete files calculus
# @dp.callback_query_handler(text='delete_files_calculus', chat_id=moderators)
# async def delete_files_calculus(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_calculus)
#
# @dp.callback_query_handler(text='delete_files_calculus_classes', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/Classes'
#     await call.message.answer(f'<b>➖ List of the files from calculus classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_classes.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Calculus/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from calculus classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_homework', chat_id=moderators)
# async def delete_files_calculus_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/Homework'
#     await call.message.answer(f'<b>➖ List of the files from calculus homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_homework.file)
# async def delete_files_calculus_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Calculus/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from calculus homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_books', chat_id=moderators)
# async def delete_files_calculus_books(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/Books'
#     await call.message.answer(f'<b>➖ List of the files from calculus books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_books.file)
# async def delete_files_calculus_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Calculus/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from calculus books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus)
#         await state.finish()
#
# # delete files statistics
# @dp.callback_query_handler(text='delete_files_statistics', chat_id=moderators)
# async def delete_files_statistics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_statistics)
#
# @dp.callback_query_handler(text='delete_files_statistics_classes', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/Classes'
#     await call.message.answer(f'<b>➖ List of the files from statistics classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_classes.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Statistics/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from statistics classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_homework', chat_id=moderators)
# async def delete_files_statistics_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/Homework'
#     await call.message.answer(f'<b>➖ List of the files from statistics homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_homework.file)
# async def delete_files_statistics_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Statistics/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from statistics homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_books', chat_id=moderators)
# async def delete_files_statistics_books(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/Books'
#     await call.message.answer(f'<b>➖ List of the files from statistics books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_books.file)
# async def delete_files_statistics_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Statistics/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from statistics books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics)
#         await state.finish()
#
# # delete files microeconomics
# @dp.callback_query_handler(text='delete_files_microeconomics', chat_id=moderators)
# async def delete_files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_microeconomics)
#
# @dp.callback_query_handler(text='delete_files_microeconomics_classes', chat_id=moderators)
# async def delete_files_microeconomics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Microeconomics/Classes'
#     await call.message.answer(f'<b>➖ List of the files from microeconomics classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_microeconomics_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_classes.file)
# async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Microeconomics/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from microeconomics classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_microeconomics_homework', chat_id=moderators)
# async def delete_files_microeconomics_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/Microeconomics/Homework'
#     await call.message.answer(f'<b>➖ List of the files from microeconomics homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_microeconomics_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_homework.file)
# async def delete_files_microeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Microeconomics/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from microeconomics homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_microeconomics_books', chat_id=moderators)
# async def delete_files_microeconomics_books(call: types.CallbackQuery):
#     path = '/root/bot/media/Microeconomics/Books'
#     await call.message.answer(f'<b>➖ List of the files from microeconomics books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_microeconomics_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_books.file)
# async def delete_files_microeconomics_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Microeconomics/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from microeconomics books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_microeconomics)
#         await state.finish()
#
# # delete files macroeconomics
# @dp.callback_query_handler(text='delete_files_macroeconomics', chat_id=moderators)
# async def delete_files_macroeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_macroeconomics)
#
# @dp.callback_query_handler(text='delete_files_macroeconomics_classes', chat_id=moderators)
# async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Macroeconomics/Classes'
#     await call.message.answer(f'<b>➖ List of the files from macroeconomics classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_macroeconomics_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_classes.file)
# async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Macroeconomics/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from macroeconomics classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_macroeconomics_homework', chat_id=moderators)
# async def delete_files_macroeconomics_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/Macroeconomics/Homework'
#     await call.message.answer(f'<b>➖ List of the files from macroeconomics homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_macroeconomics_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_homework.file)
# async def delete_files_macroeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Macroeconomics/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from macroeconomics homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_macroeconomics_books', chat_id=moderators)
# async def delete_files_macroeconomics_books(call: types.CallbackQuery):
#     path = '/root/bot/media/Macroeconomics/Books'
#     await call.message.answer(f'<b>➖ List of the files from macroeconomics books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_macroeconomics_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_books.file)
# async def delete_files_macroeconomics_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Macroeconomics/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from macroeconomics books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_macroeconomics)
#         await state.finish()
#
# # delete files history
# @dp.callback_query_handler(text='delete_files_history', chat_id=moderators)
# async def delete_files_history(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_history)
#
# @dp.callback_query_handler(text='delete_files_history_classes', chat_id=moderators)
# async def delete_files_history_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/History/Classes'
#     await call.message.answer(f'<b>➖ List of the files from history classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_history_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_classes.file)
# async def delete_files_history_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/History/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from history classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_history)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_history_homework', chat_id=moderators)
# async def delete_files_history_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/History/Homework'
#     await call.message.answer(f'<b>➖ List of the files from history homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_history_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_homework.file)
# async def delete_files_history_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/History/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from history homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_history)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_history_books', chat_id=moderators)
# async def delete_files_history_books(call: types.CallbackQuery):
#     path = '/root/bot/media/History/Books'
#     await call.message.answer(f'<b>➖ List of the files from history books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_history_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_books.file)
# async def delete_files_history_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/History/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from history books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_history)
#         await state.finish()
#
# # delete files philosophy
# @dp.callback_query_handler(text='delete_files_philosophy', chat_id=moderators)
# async def delete_files_philosophy(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_philosophy)
#
# @dp.callback_query_handler(text='delete_files_philosophy_classes', chat_id=moderators)
# async def delete_files_philosophy_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Philosophy/Classes'
#     await call.message.answer(f'<b>➖ List of the files from philosophy classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_philosophy_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_classes.file)
# async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Philosophy/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from philosophy classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_philosophy_homework', chat_id=moderators)
# async def delete_files_philosophy_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/philosophy/Homework'
#     await call.message.answer(f'<b>➖ List of the files from philosophy homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_philosophy_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_homework.file)
# async def delete_files_philosophy_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Philosophy/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from philosophy homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_philosophy_books', chat_id=moderators)
# async def delete_files_philosophy_books(call: types.CallbackQuery):
#     path = '/root/bot/media/Philosophy/Books'
#     await call.message.answer(f'<b>➖ List of the files from philosophy books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_philosophy_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_books.file)
# async def delete_files_philosophy_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/Philosophy/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from philosophy books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_philosophy)
#         await state.finish()
#
# # delete files english
# @dp.callback_query_handler(text='delete_files_english', chat_id=moderators)
# async def delete_files_english(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_english)
#
# @dp.callback_query_handler(text='delete_files_english_classes', chat_id=moderators)
# async def delete_files_english_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/English/Classes'
#     await call.message.answer(f'<b>➖ List of the files from english classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_english_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_english_classes.file)
# async def delete_files_english_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/English/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from english classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_english)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_english)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_english_homework', chat_id=moderators)
# async def delete_files_english_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/English/Homework'
#     await call.message.answer(f'<b>➖ List of the files from english homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_english_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_english_homework.file)
# async def delete_files_english_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/English/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from english homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_english)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_english)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_english_books', chat_id=moderators)
# async def delete_files_english_books(call: types.CallbackQuery):
#     path = '/root/bot/media/English/Books'
#     await call.message.answer(f'<b>➖ List of the files from english books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_english_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_english_books.file)
# async def delete_files_english_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/English/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from english books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_english)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_english)
#         await state.finish()
#
# # delete files ICS
# @dp.callback_query_handler(text='delete_files_ics', chat_id=moderators)
# async def delete_files_ics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_ics)
#
# @dp.callback_query_handler(text='delete_files_ics_classes', chat_id=moderators)
# async def delete_files_ics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/ICS/Classes'
#     await call.message.answer(f'<b>➖ List of the files from ICS classes:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_ics_classes.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_classes.file)
# async def delete_files_ics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/ICS/Classes/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS classes.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_ics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_ics_homework', chat_id=moderators)
# async def delete_files_ics_homework(call: types.CallbackQuery):
#     path = '/root/bot/media/ICS/Homework'
#     await call.message.answer(f'<b>➖ List of the files from ICS homework:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_ics_homework.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_homework.file)
# async def delete_files_ics_homework(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/ICS/Homework/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS homework.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_ics)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_ics_books', chat_id=moderators)
# async def delete_files_ics_books(call: types.CallbackQuery):
#     path = '/root/bot/media/ICS/Books'
#     await call.message.answer(f'<b>➖ List of the files from ICS books:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_ics_books.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_books.file)
# async def delete_files_ics_books(message: types.Message, state: FSMContext):
#     file_name = message.text
#     # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     try:
#         path = f'/root/bot/media/ICS/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_ics)
#         await state.finish()
#
# # deleting files back
# @dp.callback_query_handler(text='delete_files_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>🗂 Manager of the files:</b>', reply_markup=ikb_files_manager)
#
# @dp.callback_query_handler(text='delete_files_calculus_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_statistics_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_microeconomics_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_macroeconomics_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_history_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_philosophy_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_english_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
# @dp.callback_query_handler(text='delete_files_ics_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)
#
#
#
#
#
# # ---------------- adding files
# @dp.callback_query_handler(text='add_files', chat_id=moderators)
# async def delete_files_command(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>'
#                                  , reply_markup=ikb_files_subjects)
#
# # adding files calculus
# @dp.callback_query_handler(text='files_calculus', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='files_calculus_classes', chat_id=moderators)
# async def files_calculus_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in calculus classes:</b>')
#     await calculus_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_classes.file)
# async def files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in calculus classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_calculus_classes)
#
# @dp.callback_query_handler(text='send_notification_calculus_classes', chat_id=moderators, state=calculus_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}">ㅤ</a>'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='files_calculus_homework', chat_id=moderators)
# async def files_calculus_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in calculus homework:</b>')
#     await calculus_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_homework.file)
# async def files_calculus_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in calculus homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_calculus_homework)
#
# @dp.callback_query_handler(text='send_notification_calculus_homework', chat_id=moderators, state=calculus_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='files_calculus_books', chat_id=moderators)
# async def files_calculus_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in calculus books:</b>')
#     await calculus_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_books.file)
# async def files_calculus_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in calculus books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_calculus_books)
#
# @dp.callback_query_handler(text='send_notification_calculus_books', chat_id=moderators, state=calculus_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📘 Calculus books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus)
#
# # adding files statistics
# @dp.callback_query_handler(text='files_statistics', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='files_statistics_classes', chat_id=moderators)
# async def files_statistics_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in statistics classes:</b>')
#     await statistics_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_classes.file)
# async def files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in statistics classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_statistics_classes)
#
# @dp.callback_query_handler(text='send_notification_statistics_classes', chat_id=moderators, state=statistics_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='files_statistics_homework', chat_id=moderators)
# async def files_statistics_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in statistics homework:</b>')
#     await statistics_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_homework.file)
# async def files_statistics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in statistics homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_statistics_homework)
#
# @dp.callback_query_handler(text='send_notification_statistics_homework', chat_id=moderators, state=statistics_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='files_statistics_books', chat_id=moderators)
# async def files_statistics_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in statistics books:</b>')
#     await statistics_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_books.file)
# async def files_statistics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in statistics books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_statistics_books)
#
# @dp.callback_query_handler(text='send_notification_statistics_books', chat_id=moderators, state=statistics_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📗 Statistics books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics)
#
# # adding files microeconomics
# @dp.callback_query_handler(text='files_microeconomics', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='files_microeconomics_classes', chat_id=moderators)
# async def files_microeconomics_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in microeconomics classes:</b>')
#     await microeconomics_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_classes.file)
# async def files_microeconomics_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in microeconomics classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_microeconomics_classes)
#
# @dp.callback_query_handler(text='send_notification_microeconomics_classes', chat_id=moderators, state=microeconomics_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='files_microeconomics_homework', chat_id=moderators)
# async def files_microeconomics_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in microeconomics homework:</b>')
#     await microeconomics_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_homework.file)
# async def files_microeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in microeconomics homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_microeconomics_homework)
#
# @dp.callback_query_handler(text='send_notification_microeconomics_homework', chat_id=moderators, state=microeconomics_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='files_microeconomics_books', chat_id=moderators)
# async def files_microeconomics_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in microeconomics books:</b>')
#     await microeconomics_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_books.file)
# async def files_microeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in microeconomics books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_microeconomics_books)
#
# @dp.callback_query_handler(text='send_notification_microeconomics_books', chat_id=moderators, state=microeconomics_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📙 Microeconomics books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics)
#
# # adding files macroeconomics
# @dp.callback_query_handler(text='files_macroeconomics', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='files_macroeconomics_classes', chat_id=moderators)
# async def files_macroeconomics_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in macroeconomics classes:</b>')
#     await macroeconomics_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_classes.file)
# async def files_macroeconomics_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in macroeconomics classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_macroeconomics_classes)
#
# @dp.callback_query_handler(text='send_notification_macroeconomics_classes', chat_id=moderators, state=macroeconomics_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='files_macroeconomics_homework', chat_id=moderators)
# async def files_macroeconomics_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in macroeconomics homework:</b>')
#     await macroeconomics_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_homework.file)
# async def files_macroeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in macroeconomics homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_macroeconomics_homework)
#
# @dp.callback_query_handler(text='send_notification_macroeconomics_homework', chat_id=moderators, state=macroeconomics_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='files_macroeconomics_books', chat_id=moderators)
# async def files_macroeconomics_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in macroeconomics books:</b>')
#     await macroeconomics_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_books.file)
# async def files_macroeconomics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in macroeconomics books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_macroeconomics_books)
#
# @dp.callback_query_handler(text='send_notification_macroeconomics_books', chat_id=moderators, state=macroeconomics_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📕 Macroeconomics books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics)
#
# # adding files history
# @dp.callback_query_handler(text='files_history', chat_id=moderators)
# async def files_history(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='files_history_classes', chat_id=moderators)
# async def files_history_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in history classes:</b>')
#     await history_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_classes.file)
# async def files_history_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in history classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_history_classes)
#
# @dp.callback_query_handler(text='send_notification_history_classes', chat_id=moderators, state=history_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='files_history_homework', chat_id=moderators)
# async def files_history_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in history homework:</b>')
#     await history_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_homework.file)
# async def files_history_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in history homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_history_homework)
#
# @dp.callback_query_handler(text='send_notification_history_homework', chat_id=moderators, state=history_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='files_history_books', chat_id=moderators)
# async def files_history_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in history books:</b>')
#     await history_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_books.file)
# async def files_history_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in history books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_history_books)
#
# @dp.callback_query_handler(text='send_notification_history_books', chat_id=moderators, state=history_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📔 History books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history)
#
# # adding files philosophy
# @dp.callback_query_handler(text='files_philosophy', chat_id=moderators)
# async def files_philosophy(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='files_philosophy_classes', chat_id=moderators)
# async def files_philosophy_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in philosophy classes:</b>')
#     await philosophy_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_classes.file)
# async def files_philosophy_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in philosophy classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_philosophy_classes)
#
# @dp.callback_query_handler(text='send_notification_philosophy_classes', chat_id=moderators, state=philosophy_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='files_philosophy_homework', chat_id=moderators)
# async def files_philosophy_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in philosophy homework:</b>')
#     await philosophy_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_homework.file)
# async def files_philosophy_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in philosophy homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_philosophy_homework)
#
# @dp.callback_query_handler(text='send_notification_philosophy_homework', chat_id=moderators, state=philosophy_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='files_philosophy_books', chat_id=moderators)
# async def files_philosophy_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in philosophy books:</b>')
#     await philosophy_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_books.file)
# async def files_philosophy_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in philosophy books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_philosophy_books)
#
# @dp.callback_query_handler(text='send_notification_philosophy_books', chat_id=moderators, state=philosophy_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📒 Philosophy books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy)
#
# # adding files english
# @dp.callback_query_handler(text='files_english', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='files_english_classes', chat_id=moderators)
# async def files_english_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in english classes:</b>')
#     await english_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=english_classes.file)
# async def files_english_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/English/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in english classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_english_classes)
#
# @dp.callback_query_handler(text='send_notification_english_classes', chat_id=moderators, state=english_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>🇬🇧 English classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='files_english_homework', chat_id=moderators)
# async def files_english_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in english homework:</b>')
#     await english_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=english_homework.file)
# async def files_english_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/English/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in english homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_english_homework)
#
# @dp.callback_query_handler(text='send_notification_english_homework', chat_id=moderators, state=english_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>🇬🇧 English homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='files_english_books', chat_id=moderators)
# async def files_english_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in english books:</b>')
#     await english_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=english_books.file)
# async def files_english_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/English/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in english books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_english_books)
#
# @dp.callback_query_handler(text='send_notification_english_books', chat_id=moderators, state=english_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>🇬🇧 English books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# # adding files ICS
# @dp.callback_query_handler(text='files_ics', chat_id=moderators)
# async def files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='files_ics_classes', chat_id=moderators)
# async def files_ics_classes(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS classes:</b>')
#     await ics_classes.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_classes.file)
# async def files_ics_classes(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/Classes/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in ICS classes.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_ics_classes)
#
# @dp.callback_query_handler(text='send_notification_ics_classes', chat_id=moderators, state=ics_classes.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS classes were updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='files_ics_homework', chat_id=moderators)
# async def files_ics_homework(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS homework:</b>')
#     await ics_homework.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_homework.file)
# async def files_ics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/Homework/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in ICS homework.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_ics_homework)
#
# @dp.callback_query_handler(text='send_notification_ics_homework', chat_id=moderators, state=ics_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS homework was updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='files_ics_books', chat_id=moderators)
# async def files_ics_books(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS books:</b>')
#     await ics_books.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_books.file)
# async def files_ics_homework(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/Books/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" was added in ICS books.</b>')
#         await message.answer('<b>🔊 Send notification?</b>', reply_markup=ikb_files_notification_ics_books)
#
# @dp.callback_query_handler(text='send_notification_ics_books', chat_id=moderators, state=ics_books.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#     users = await quick_commands.select_all_users()
#     data = await state.get_data()
#     file_name = data.get('file_name')
#     text = f'<b>📓 ICS books were updated.</b>\n\n' \
#            f'<b>Added file:</b> {file_name}'
#     await state.finish()
#     for user in users:
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     await call.message.edit_text('<b>🔊 Notification is sent.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>❌ Notification is canceled.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics)
#
# # adding files back
# @dp.callback_query_handler(text='files_back', chat_id=moderators)
# async def files_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>🗂 Manager of the files:</b>', reply_markup=ikb_files_manager)
#
# @dp.callback_query_handler(text='files_calculus_back', chat_id=moderators)
# async def files_calculus_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_statistics_back', chat_id=moderators)
# async def files_statistics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_microeconomics_back', chat_id=moderators)
# async def files_microeconomics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_macroeconomics_back', chat_id=moderators)
# async def files_macroeconomics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_history_back', chat_id=moderators)
# async def files_ics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_philosophy_back', chat_id=moderators)
# async def files_ics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_english_back', chat_id=moderators)
# async def files_english_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
# @dp.callback_query_handler(text='files_ics_back', chat_id=moderators)
# async def files_ics_cancel(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)
#
#
