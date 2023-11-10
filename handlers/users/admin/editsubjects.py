import os
import shutil

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_keyboard_settings import ikb_settings_admins, ikb_settings_admins_subjects
from loader import dp

from data.config import moderators
from filters import IsPrivateMessage
from utils.db_api import quick_commands
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
#     ikb_files_notification_philosophy_classes, ikb_files_subjects, ikb_files_calculus, ikb_files_manager, \
#     ikb_files_calculus2
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

from keyboards.inline.inline_keyboard_files_subjects import ikb_files_manager, ikb_files_subjects, ikb_delete_files_subjects, ikb_files_notification_calculus_books, ikb_files_notification_statistics_books, ikb_files_notification_microeconomics_books, ikb_files_notification_macroeconomics_books, ikb_files_notification_history_books, ikb_files_notification_philosophy_books, ikb_files_notification_ics_books
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_calculus2, ikb_files_statistics2, ikb_files_microeconomics2, ikb_files_macroeconomics2, ikb_files_history2, ikb_files_philosophy2, ikb_files_ics2
from keyboards.inline.inline_keyboard_files_subjects import ikb_delete_files_calculus2, ikb_delete_files_statistics2, ikb_delete_files_microeconomics2, ikb_delete_files_macroeconomics2, ikb_delete_files_history2, ikb_delete_files_philosophy2, ikb_delete_files_ics2
from keyboards.inline.inline_keyboard_files_subjects import ikb_delete_files_calculus2, ikb_delete_files_statistics2, ikb_delete_files_microeconomics2, ikb_delete_files_macroeconomics2, ikb_delete_files_history2, ikb_delete_files_philosophy2, ikb_delete_files_ics2
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_calculus_1, ikb_files_notification_calculus_2, ikb_files_notification_calculus_3, ikb_files_notification_calculus_4, ikb_files_notification_calculus_5, ikb_files_notification_calculus_6, ikb_files_notification_calculus_7, ikb_files_notification_calculus_8, ikb_files_notification_calculus_9, ikb_files_notification_calculus_10, ikb_files_notification_calculus_11, ikb_files_notification_calculus_12, ikb_files_notification_calculus_13, ikb_files_notification_calculus_14, ikb_files_notification_calculus_15, ikb_files_notification_calculus_16, ikb_files_notification_calculus_17, ikb_files_notification_calculus_18, ikb_files_notification_calculus_19, ikb_files_notification_calculus_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_statistics_1, ikb_files_notification_statistics_2, ikb_files_notification_statistics_3, ikb_files_notification_statistics_4, ikb_files_notification_statistics_5, ikb_files_notification_statistics_6, ikb_files_notification_statistics_7, ikb_files_notification_statistics_8, ikb_files_notification_statistics_9, ikb_files_notification_statistics_10, ikb_files_notification_statistics_11, ikb_files_notification_statistics_12, ikb_files_notification_statistics_13, ikb_files_notification_statistics_14, ikb_files_notification_statistics_15, ikb_files_notification_statistics_16, ikb_files_notification_statistics_17, ikb_files_notification_statistics_18, ikb_files_notification_statistics_19, ikb_files_notification_statistics_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_microeconomics_1, ikb_files_notification_microeconomics_2, ikb_files_notification_microeconomics_3, ikb_files_notification_microeconomics_4, ikb_files_notification_microeconomics_5, ikb_files_notification_microeconomics_6, ikb_files_notification_microeconomics_7, ikb_files_notification_microeconomics_8, ikb_files_notification_microeconomics_9, ikb_files_notification_microeconomics_10, ikb_files_notification_microeconomics_11, ikb_files_notification_microeconomics_12, ikb_files_notification_microeconomics_13, ikb_files_notification_microeconomics_14, ikb_files_notification_microeconomics_15, ikb_files_notification_microeconomics_16, ikb_files_notification_microeconomics_17, ikb_files_notification_microeconomics_18, ikb_files_notification_microeconomics_19, ikb_files_notification_microeconomics_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_macroeconomics_1, ikb_files_notification_macroeconomics_2, ikb_files_notification_macroeconomics_3, ikb_files_notification_macroeconomics_4, ikb_files_notification_macroeconomics_5, ikb_files_notification_macroeconomics_6, ikb_files_notification_macroeconomics_7, ikb_files_notification_macroeconomics_8, ikb_files_notification_macroeconomics_9, ikb_files_notification_macroeconomics_10, ikb_files_notification_macroeconomics_11, ikb_files_notification_macroeconomics_12, ikb_files_notification_macroeconomics_13, ikb_files_notification_macroeconomics_14, ikb_files_notification_macroeconomics_15, ikb_files_notification_macroeconomics_16, ikb_files_notification_macroeconomics_17, ikb_files_notification_macroeconomics_18, ikb_files_notification_macroeconomics_19, ikb_files_notification_macroeconomics_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_history_1, ikb_files_notification_history_2, ikb_files_notification_history_3, ikb_files_notification_history_4, ikb_files_notification_history_5, ikb_files_notification_history_6, ikb_files_notification_history_7, ikb_files_notification_history_8, ikb_files_notification_history_9, ikb_files_notification_history_10, ikb_files_notification_history_11, ikb_files_notification_history_12, ikb_files_notification_history_13, ikb_files_notification_history_14, ikb_files_notification_history_15, ikb_files_notification_history_16, ikb_files_notification_history_17, ikb_files_notification_history_18, ikb_files_notification_history_19, ikb_files_notification_history_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_philosophy_1, ikb_files_notification_philosophy_2, ikb_files_notification_philosophy_3, ikb_files_notification_philosophy_4, ikb_files_notification_philosophy_5, ikb_files_notification_philosophy_6, ikb_files_notification_philosophy_7, ikb_files_notification_philosophy_8, ikb_files_notification_philosophy_9, ikb_files_notification_philosophy_10, ikb_files_notification_philosophy_11, ikb_files_notification_philosophy_12, ikb_files_notification_philosophy_13, ikb_files_notification_philosophy_14, ikb_files_notification_philosophy_15, ikb_files_notification_philosophy_16, ikb_files_notification_philosophy_17, ikb_files_notification_philosophy_18, ikb_files_notification_philosophy_19, ikb_files_notification_philosophy_20
from keyboards.inline.inline_keyboard_files_subjects import ikb_files_notification_ics_1, ikb_files_notification_ics_2, ikb_files_notification_ics_3, ikb_files_notification_ics_4, ikb_files_notification_ics_5, ikb_files_notification_ics_6, ikb_files_notification_ics_7, ikb_files_notification_ics_8, ikb_files_notification_ics_9, ikb_files_notification_ics_10, ikb_files_notification_ics_11, ikb_files_notification_ics_12, ikb_files_notification_ics_13, ikb_files_notification_ics_14, ikb_files_notification_ics_15, ikb_files_notification_ics_16, ikb_files_notification_ics_17, ikb_files_notification_ics_18, ikb_files_notification_ics_19, ikb_files_notification_ics_20


from states.files import calculus_books, statistics_books, microeconomics_books, macroeconomics_books, history_books, philosophy_books, ics_books, delete_calculus_books, delete_statistics_books, delete_microeconomics_books, delete_macroeconomics_books, delete_history_books, delete_philosophy_books, delete_ics_books
from states.files import calculus_1, calculus_2, calculus_3, calculus_4, calculus_5, calculus_6, calculus_7, calculus_8, calculus_9, calculus_10, calculus_11, calculus_12, calculus_13, calculus_14, calculus_15, calculus_16, calculus_17, calculus_18, calculus_19, calculus_20, delete_calculus_1, delete_calculus_2, delete_calculus_3, delete_calculus_4, delete_calculus_5, delete_calculus_6, delete_calculus_7, delete_calculus_8, delete_calculus_9, delete_calculus_10, delete_calculus_11, delete_calculus_12, delete_calculus_13, delete_calculus_14, delete_calculus_15, delete_calculus_16, delete_calculus_17, delete_calculus_18, delete_calculus_19, delete_calculus_20
from states.files import statistics_1, statistics_2, statistics_3, statistics_4, statistics_5, statistics_6, statistics_7, statistics_8, statistics_9, statistics_10, statistics_11, statistics_12, statistics_13, statistics_14, statistics_15, statistics_16, statistics_17, statistics_18, statistics_19, statistics_20, delete_statistics_1, delete_statistics_2, delete_statistics_3, delete_statistics_4, delete_statistics_5, delete_statistics_6, delete_statistics_7, delete_statistics_8, delete_statistics_9, delete_statistics_10, delete_statistics_11, delete_statistics_12, delete_statistics_13, delete_statistics_14, delete_statistics_15, delete_statistics_16, delete_statistics_17, delete_statistics_18, delete_statistics_19, delete_statistics_20
from states.files import microeconomics_1, microeconomics_2, microeconomics_3, microeconomics_4, microeconomics_5, microeconomics_6, microeconomics_7, microeconomics_8, microeconomics_9, microeconomics_10, microeconomics_11, microeconomics_12, microeconomics_13, microeconomics_14, microeconomics_15, microeconomics_16, microeconomics_17, microeconomics_18, microeconomics_19, microeconomics_20, delete_microeconomics_1, delete_microeconomics_2, delete_microeconomics_3, delete_microeconomics_4, delete_microeconomics_5, delete_microeconomics_6, delete_microeconomics_7, delete_microeconomics_8, delete_microeconomics_9, delete_microeconomics_10, delete_microeconomics_11, delete_microeconomics_12, delete_microeconomics_13, delete_microeconomics_14, delete_microeconomics_15, delete_microeconomics_16, delete_microeconomics_17, delete_microeconomics_18, delete_microeconomics_19, delete_microeconomics_20
from states.files import macroeconomics_1, macroeconomics_2, macroeconomics_3, macroeconomics_4, macroeconomics_5, macroeconomics_6, macroeconomics_7, macroeconomics_8, macroeconomics_9, macroeconomics_10, macroeconomics_11, macroeconomics_12, macroeconomics_13, macroeconomics_14, macroeconomics_15, macroeconomics_16, macroeconomics_17, macroeconomics_18, macroeconomics_19, macroeconomics_20, delete_macroeconomics_1, delete_macroeconomics_2, delete_macroeconomics_3, delete_macroeconomics_4, delete_macroeconomics_5, delete_macroeconomics_6, delete_macroeconomics_7, delete_macroeconomics_8, delete_macroeconomics_9, delete_macroeconomics_10, delete_macroeconomics_11, delete_macroeconomics_12, delete_macroeconomics_13, delete_macroeconomics_14, delete_macroeconomics_15, delete_macroeconomics_16, delete_macroeconomics_17, delete_macroeconomics_18, delete_macroeconomics_19, delete_macroeconomics_20
from states.files import history_1, history_2, history_3, history_4, history_5, history_6, history_7, history_8, history_9, history_10, history_11, history_12, history_13, history_14, history_15, history_16, history_17, history_18, history_19, history_20, delete_history_1, delete_history_2, delete_history_3, delete_history_4, delete_history_5, delete_history_6, delete_history_7, delete_history_8, delete_history_9, delete_history_10, delete_history_11, delete_history_12, delete_history_13, delete_history_14, delete_history_15, delete_history_16, delete_history_17, delete_history_18, delete_history_19, delete_history_20
from states.files import philosophy_1, philosophy_2, philosophy_3, philosophy_4, philosophy_5, philosophy_6, philosophy_7, philosophy_8, philosophy_9, philosophy_10, philosophy_11, philosophy_12, philosophy_13, philosophy_14, philosophy_15, philosophy_16, philosophy_17, philosophy_18, philosophy_19, philosophy_20, delete_philosophy_1, delete_philosophy_2, delete_philosophy_3, delete_philosophy_4, delete_philosophy_5, delete_philosophy_6, delete_philosophy_7, delete_philosophy_8, delete_philosophy_9, delete_philosophy_10, delete_philosophy_11, delete_philosophy_12, delete_philosophy_13, delete_philosophy_14, delete_philosophy_15, delete_philosophy_16, delete_philosophy_17, delete_philosophy_18, delete_philosophy_19, delete_philosophy_20
from states.files import ics_1, ics_2, ics_3, ics_4, ics_5, ics_6, ics_7, ics_8, ics_9, ics_10, ics_11, ics_12, ics_13, ics_14, ics_15, ics_16, ics_17, ics_18, ics_19, ics_20, delete_ics_1, delete_ics_2, delete_ics_3, delete_ics_4, delete_ics_5, delete_ics_6, delete_ics_7, delete_ics_8, delete_ics_9, delete_ics_10, delete_ics_11, delete_ics_12, delete_ics_13, delete_ics_14, delete_ics_15, delete_ics_16, delete_ics_17, delete_ics_18, delete_ics_19, delete_ics_20



# files manager
@dp.callback_query_handler(text='edit_subjects')
async def admin_panel_back(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>📚 Editing of subjects:</b>', reply_markup=ikb_settings_admins_subjects)

@dp.callback_query_handler(text='edit_subjects_files', chat_id=moderators)
async def files_manager_command(call: types.CallbackQuery):
    await call.message.edit_text('<b>📚 Editing of subjects - <ins>files</ins>:</b>'
                         , reply_markup=ikb_files_manager)

@dp.callback_query_handler(text='files_back', chat_id=moderators)
async def admin_panel_back(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>📚 Editing of subjects:</b>', reply_markup=ikb_settings_admins_subjects)

# ------------------ delete files
@dp.callback_query_handler(text='delete_files', chat_id=moderators)
async def delete_files_command(call: types.CallbackQuery):
    await call.message.edit_text('<b>➖ Deleting of the files:</b>'
                                 , reply_markup=ikb_delete_files_subjects)

# delete files calculus
# @dp.callback_query_handler(text='delete_files_calculus', chat_id=moderators)
# async def delete_files_calculus(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_calculus2)

@dp.callback_query_handler(text='delete_files_calculus', chat_id=moderators)
async def delete_files_calculus(call: types.CallbackQuery):
    path = '/root/bot/media/Calculus'
    await call.message.answer(f'<b>➖ List of the files from Calculus:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_calculus_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_1.file)
async def delete_files_calculus_state(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Calculus/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_calculus2)
        await state.finish()

# @dp.callback_query_handler(text='delete_files_calculus_2', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/2'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 2nd week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_2.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_2.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/2/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 2nd week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_3', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/3'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 3rd week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_3.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_3.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/3/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 3rd week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_4', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/4'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 4th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_4.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_4.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/4/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 4th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_5', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/5'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 5th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_5.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_5.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/5/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 5th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_6', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/6'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 6th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_6.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_6.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/6/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 6th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_7', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/7'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 7th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_7.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_7.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/7/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 7th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_8', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/8'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 8th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_8.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_8.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/8/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 8th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_9', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/9'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 9th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_9.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_9.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/9/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 9th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_10', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/10'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 10th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_10.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_10.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/10/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 10th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_11', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/11'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 11th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_11.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_11.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/11/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 11th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_12', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/12'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 12th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_12.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_12.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/12/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 12th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_13', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/13'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 13th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_13.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_13.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/13/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 13th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_14', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/14'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 14th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_14.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_14.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/14/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 14th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_15', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/15'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 15th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_15.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_15.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/15/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 15th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_16', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/16'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 16th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_16.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_16.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/16/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 16th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_17', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/17'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 17th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_17.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_17.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/17/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 17th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_18', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/18'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 18th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_18.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_18.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/18/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 18th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_19', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/19'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 19th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_19.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_19.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/19/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 19th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_calculus_20', chat_id=moderators)
# async def delete_files_calculus_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Calculus/20'
#     await call.message.answer(f'<b>➖ List of the files from Calculus, 20th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_calculus_20.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_calculus_20.file)
# async def delete_files_calculus_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Calculus/20/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Calculus, 20th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
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
#     try:
#         path = f'/root/bot/media/Calculus/Books/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from calculus books.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_calculus2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_calculus2)
#         await state.finish()

# delete files statistics
# @dp.callback_query_handler(text='delete_files_statistics', chat_id=moderators)
# async def delete_files_statistics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_statistics2)

@dp.callback_query_handler(text='delete_files_statistics', chat_id=moderators)
async def delete_files_statistics(call: types.CallbackQuery):
    path = '/root/bot/media/Statistics'
    await call.message.answer(f'<b>➖ List of the files from Statistics:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_statistics_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_1.file)
async def delete_files_statistics_state(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Statistics/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_statistics2)
        await state.finish()

# @dp.callback_query_handler(text='delete_files_statistics_2', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/2'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 2nd week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_2.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_2.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/2/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 2nd week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_3', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/3'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 3rd week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_3.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_3.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/3/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 3rd week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_4', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/4'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 4th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_4.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_4.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/4/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 4th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_5', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/5'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 5th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_5.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_5.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/5/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 5th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_6', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/6'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 6th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_6.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_6.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/6/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 6th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_7', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/7'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 7th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_7.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_7.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/7/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 7th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_8', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/8'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 8th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_8.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_8.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/8/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 8th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_9', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/9'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 9th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_9.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_9.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/9/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 9th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_10', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/10'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 10th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_10.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_10.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/10/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 10th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_11', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/11'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 11th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_11.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_11.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/11/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 11th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_12', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/12'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 12th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_12.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_12.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/12/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 12th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_13', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/13'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 13th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_13.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_13.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/13/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 13th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_14', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/14'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 14th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_14.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_14.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/14/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 14th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_15', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/15'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 15th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_15.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_15.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/15/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 15th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_16', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/16'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 16th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_16.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_16.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/16/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 16th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_17', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/17'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 17th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_17.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_17.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/17/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 17th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_18', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/18'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 18th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_18.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_18.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/18/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 18th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_19', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/19'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 19th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_19.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_19.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/19/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 19th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#
# @dp.callback_query_handler(text='delete_files_statistics_20', chat_id=moderators)
# async def delete_files_statistics_classes(call: types.CallbackQuery):
#     path = '/root/bot/media/Statistics/20'
#     await call.message.answer(f'<b>➖ List of the files from Statistics, 20th week:</b>')
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             await call.message.answer(filename)
#         await call.message.answer('<b>➖ Enter a file name to delete:</b>')
#         await delete_statistics_20.file.set()
#
# @dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_statistics_20.file)
# async def delete_files_statistics_classes(message: types.Message, state: FSMContext):
#     file_name = message.text
#     try:
#         path = f'/root/bot/media/Statistics/20/{file_name}'
#         os.remove(path)
#         await message.answer(f'<b>➖ File "{file_name}" was deleted from Statistics, 20th week.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
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
#         await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_statistics2)
#         await state.finish()
#     except FileNotFoundError:
#         await message.answer('<b>⚠️ There is no such file.</b>')
#         await message.answer('<b>➖ Deleting of the files:</b>'
#                                      , reply_markup=ikb_delete_files_statistics2)
#         await state.finish()

# delete files Microeconomics
# @dp.callback_query_handler(text='delete_files_microeconomics', chat_id=moderators)
# async def delete_files_microeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➖ Deleting of the files:</b>'
#                                  , reply_markup=ikb_delete_files_microeconomics2)

@dp.callback_query_handler(text='delete_files_microeconomics', chat_id=moderators)
async def delete_files_microeconomics(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics.</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_1.file)
async def delete_files_microeconomics_state(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_2', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/2'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 2nd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_2.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_2.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/2/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 2nd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_3', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/3'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 3rd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_3.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_3.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/3/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 3rd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_4', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/4'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 4th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_4.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_4.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/4/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 4th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_5', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/5'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 5th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_5.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_5.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/5/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 5th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_6', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/6'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 6th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_6.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_6.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/6/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 6th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_7', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/7'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 7th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_7.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_7.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/7/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 7th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_8', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/8'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 8th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_8.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_8.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/8/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 8th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_9', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/9'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 9th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_9.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_9.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/9/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 9th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_10', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/10'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 10th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_10.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_10.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/10/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 10th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_11', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/11'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 11th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_11.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_11.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/11/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 11th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_12', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/12'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 12th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_12.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_12.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/12/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 12th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_13', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/13'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 13th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_13.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_13.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/13/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 13th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_14', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/14'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 14th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_14.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_14.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/14/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 14th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_15', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/15'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 15th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_15.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_15.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/15/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 15th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_16', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/16'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 16th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_16.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_16.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/16/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 16th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_17', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/17'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 17th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_17.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_17.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/17/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 17th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_18', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/18'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 18th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_18.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_18.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/18/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 18th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_19', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/19'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 19th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_19.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_19.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/19/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 19th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_20', chat_id=moderators)
async def delete_files_microeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/20'
    await call.message.answer(f'<b>➖ List of the files from Microeconomics, 20th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_20.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_20.file)
async def delete_files_microeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Microeconomics/20/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Microeconomics, 20th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_microeconomics_books', chat_id=moderators)
async def delete_files_microeconomics_books(call: types.CallbackQuery):
    path = '/root/bot/media/Microeconomics/Books'
    await call.message.answer(f'<b>➖ List of the files from microeconomics books:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_microeconomics_books.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_microeconomics_books.file)
async def delete_files_microeconomics_books(message: types.Message, state: FSMContext):
    file_name = message.text
    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    try:
        path = f'/root/bot/media/Microeconomics/Books/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from microeconomics books.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_microeconomics2)
        await state.finish()

# delete files Macroeconomics
@dp.callback_query_handler(text='delete_files_macroeconomics', chat_id=moderators)
async def delete_files_macroeconomics(call: types.CallbackQuery):
    await call.message.edit_text('<b>➖ Deleting of the files:</b>'
                                 , reply_markup=ikb_delete_files_macroeconomics2)

@dp.callback_query_handler(text='delete_files_macroeconomics_1', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/1'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 1st week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_1.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/1/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 1st week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_2', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/2'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 2nd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_2.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_2.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/2/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 2nd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_3', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/3'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 3rd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_3.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_3.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/3/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 3rd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_4', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/4'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 4th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_4.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_4.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/4/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 4th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_5', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/5'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 5th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_5.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_5.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/5/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 5th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_6', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/6'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 6th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_6.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_6.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/6/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 6th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_7', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/7'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 7th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_7.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_7.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/7/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 7th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_8', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/8'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 8th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_8.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_8.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/8/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 8th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_9', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/9'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 9th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_9.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_9.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/9/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 9th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_10', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/10'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 10th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_10.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_10.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/10/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 10th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_11', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/11'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 11th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_11.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_11.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/11/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 11th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_12', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/12'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 12th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_12.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_12.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/12/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 12th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_13', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/13'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 13th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_13.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_13.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/13/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 13th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_14', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/14'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 14th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_14.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_14.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/14/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 14th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_15', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/15'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 15th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_15.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_15.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/15/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 15th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_16', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/16'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 16th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_16.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_16.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/16/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 16th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_17', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/17'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 17th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_17.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_17.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/17/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 17th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_18', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/18'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 18th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_18.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_18.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/18/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 18th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_19', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/19'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 19th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_19.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_19.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/19/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 19th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_20', chat_id=moderators)
async def delete_files_macroeconomics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/20'
    await call.message.answer(f'<b>➖ List of the files from Macroeconomics, 20th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_20.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_20.file)
async def delete_files_macroeconomics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Macroeconomics/20/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Macroeconomics, 20th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_macroeconomics_books', chat_id=moderators)
async def delete_files_macroeconomics_books(call: types.CallbackQuery):
    path = '/root/bot/media/Macroeconomics/Books'
    await call.message.answer(f'<b>➖ List of the files from macroeconomics books:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_macroeconomics_books.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_macroeconomics_books.file)
async def delete_files_macroeconomics_books(message: types.Message, state: FSMContext):
    file_name = message.text
    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    try:
        path = f'/root/bot/media/Macroeconomics/Books/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from macroeconomics books.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_macroeconomics2)
        await state.finish()

# delete files History
@dp.callback_query_handler(text='delete_files_history', chat_id=moderators)
async def delete_files_history(call: types.CallbackQuery):
    await call.message.edit_text('<b>➖ Deleting of the files:</b>'
                                 , reply_markup=ikb_delete_files_history2)

@dp.callback_query_handler(text='delete_files_history_1', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/1'
    await call.message.answer(f'<b>➖ List of the files from History, 1st week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_1.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/1/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 1st week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_2', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/2'
    await call.message.answer(f'<b>➖ List of the files from History, 2nd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_2.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_2.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/2/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 2nd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_3', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/3'
    await call.message.answer(f'<b>➖ List of the files from History, 3rd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_3.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_3.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/3/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 3rd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_4', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/4'
    await call.message.answer(f'<b>➖ List of the files from History, 4th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_4.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_4.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/4/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 4th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_5', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/5'
    await call.message.answer(f'<b>➖ List of the files from History, 5th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_5.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_5.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/5/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 5th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_6', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/6'
    await call.message.answer(f'<b>➖ List of the files from History, 6th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_6.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_6.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/6/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 6th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_7', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/7'
    await call.message.answer(f'<b>➖ List of the files from History, 7th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_7.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_7.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/7/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 7th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_8', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/8'
    await call.message.answer(f'<b>➖ List of the files from History, 8th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_8.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_8.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/8/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 8th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_9', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/9'
    await call.message.answer(f'<b>➖ List of the files from History, 9th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_9.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_9.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/9/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 9th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_10', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/10'
    await call.message.answer(f'<b>➖ List of the files from History, 10th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_10.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_10.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/10/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 10th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_11', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/11'
    await call.message.answer(f'<b>➖ List of the files from History, 11th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_11.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_11.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/11/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 11th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_12', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/12'
    await call.message.answer(f'<b>➖ List of the files from History, 12th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_12.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_12.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/12/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 12th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_13', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/13'
    await call.message.answer(f'<b>➖ List of the files from History, 13th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_13.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_13.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/13/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 13th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_14', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/14'
    await call.message.answer(f'<b>➖ List of the files from History, 14th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_14.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_14.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/14/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 14th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_15', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/15'
    await call.message.answer(f'<b>➖ List of the files from History, 15th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_15.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_15.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/15/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 15th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_16', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/16'
    await call.message.answer(f'<b>➖ List of the files from History, 16th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_16.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_16.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/16/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 16th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_17', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/17'
    await call.message.answer(f'<b>➖ List of the files from History, 17th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_17.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_17.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/17/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 17th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_18', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/18'
    await call.message.answer(f'<b>➖ List of the files from History, 18th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_18.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_18.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/18/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 18th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_19', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/19'
    await call.message.answer(f'<b>➖ List of the files from History, 19th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_19.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_19.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/19/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 19th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_20', chat_id=moderators)
async def delete_files_history_classes(call: types.CallbackQuery):
    path = '/root/bot/media/History/20'
    await call.message.answer(f'<b>➖ List of the files from History, 20th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_20.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_20.file)
async def delete_files_history_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/History/20/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from History, 20th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_history_books', chat_id=moderators)
async def delete_files_history_books(call: types.CallbackQuery):
    path = '/root/bot/media/History/Books'
    await call.message.answer(f'<b>➖ List of the files from history books:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_history_books.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_history_books.file)
async def delete_files_history_books(message: types.Message, state: FSMContext):
    file_name = message.text
    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    try:
        path = f'/root/bot/media/History/Books/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from history books.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_history2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_history2)
        await state.finish()

# delete files Philosophy
@dp.callback_query_handler(text='delete_files_philosophy', chat_id=moderators)
async def delete_files_philosophy(call: types.CallbackQuery):
    await call.message.edit_text('<b>➖ Deleting of the files:</b>'
                                 , reply_markup=ikb_delete_files_philosophy2)

@dp.callback_query_handler(text='delete_files_philosophy_1', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/1'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 1st week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_1.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/1/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 1st week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_2', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/2'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 2nd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_2.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_2.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/2/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 2nd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_3', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/3'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 3rd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_3.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_3.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/3/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 3rd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_4', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/4'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 4th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_4.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_4.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/4/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 4th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_5', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/5'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 5th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_5.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_5.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/5/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 5th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_6', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/6'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 6th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_6.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_6.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/6/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 6th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_7', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/7'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 7th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_7.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_7.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/7/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 7th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_8', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/8'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 8th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_8.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_8.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/8/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 8th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_9', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/9'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 9th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_9.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_9.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/9/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 9th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_10', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/10'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 10th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_10.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_10.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/10/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 10th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_11', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/11'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 11th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_11.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_11.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/11/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 11th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_12', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/12'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 12th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_12.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_12.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/12/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 12th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_13', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/13'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 13th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_13.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_13.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/13/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 13th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_14', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/14'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 14th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_14.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_14.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/14/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 14th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_15', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/15'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 15th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_15.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_15.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/15/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 15th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_16', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/16'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 16th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_16.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_16.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/16/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 16th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_17', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/17'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 17th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_17.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_17.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/17/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 17th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_18', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/18'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 18th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_18.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_18.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/18/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 18th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_19', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/19'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 19th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_19.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_19.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/19/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 19th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_20', chat_id=moderators)
async def delete_files_philosophy_classes(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/20'
    await call.message.answer(f'<b>➖ List of the files from Philosophy, 20th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_20.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_20.file)
async def delete_files_philosophy_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/Philosophy/20/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from Philosophy, 20th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_philosophy_books', chat_id=moderators)
async def delete_files_philosophy_books(call: types.CallbackQuery):
    path = '/root/bot/media/Philosophy/Books'
    await call.message.answer(f'<b>➖ List of the files from philosophy books:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_philosophy_books.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_philosophy_books.file)
async def delete_files_philosophy_books(message: types.Message, state: FSMContext):
    file_name = message.text
    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    try:
        path = f'/root/bot/media/Philosophy/Books/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from philosophy books.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_philosophy2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_philosophy2)
        await state.finish()

# delete files english
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

# delete files ICS
@dp.callback_query_handler(text='delete_files_ics', chat_id=moderators)
async def delete_files_ics(call: types.CallbackQuery):
    await call.message.edit_text('<b>➖ Deleting of the files:</b>'
                                 , reply_markup=ikb_delete_files_ics2)

@dp.callback_query_handler(text='delete_files_ics_1', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/1'
    await call.message.answer(f'<b>➖ List of the files from ICS, 1st week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_1.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_1.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/1/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 1st week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_2', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/2'
    await call.message.answer(f'<b>➖ List of the files from ICS, 2nd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_2.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_2.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/2/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 2nd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_3', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/3'
    await call.message.answer(f'<b>➖ List of the files from ICS, 3rd week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_3.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_3.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/3/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 3rd week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_4', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/4'
    await call.message.answer(f'<b>➖ List of the files from ICS, 4th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_4.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_4.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/4/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 4th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_5', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/5'
    await call.message.answer(f'<b>➖ List of the files from ICS, 5th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_5.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_5.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/5/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 5th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_6', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/6'
    await call.message.answer(f'<b>➖ List of the files from ICS, 6th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_6.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_6.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/6/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 6th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_7', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/7'
    await call.message.answer(f'<b>➖ List of the files from ICS, 7th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_7.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_7.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/7/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 7th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_8', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/8'
    await call.message.answer(f'<b>➖ List of the files from ICS, 8th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_8.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_8.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/8/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 8th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_9', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/9'
    await call.message.answer(f'<b>➖ List of the files from ICS, 9th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_9.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_9.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/9/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 9th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_10', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/10'
    await call.message.answer(f'<b>➖ List of the files from ICS, 10th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_10.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_10.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/10/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 10th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_11', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/11'
    await call.message.answer(f'<b>➖ List of the files from ICS, 11th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_11.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_11.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/11/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 11th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_12', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/12'
    await call.message.answer(f'<b>➖ List of the files from ICS, 12th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_12.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_12.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/12/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 12th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_13', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/13'
    await call.message.answer(f'<b>➖ List of the files from ICS, 13th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_13.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_13.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/13/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 13th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_14', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/14'
    await call.message.answer(f'<b>➖ List of the files from ICS, 14th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_14.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_14.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/14/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 14th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_15', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/15'
    await call.message.answer(f'<b>➖ List of the files from ICS, 15th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_15.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_15.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/15/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 15th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_16', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/16'
    await call.message.answer(f'<b>➖ List of the files from ICS, 16th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_16.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_16.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/16/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 16th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_17', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/17'
    await call.message.answer(f'<b>➖ List of the files from ICS, 17th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_17.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_17.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/17/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 17th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_18', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/18'
    await call.message.answer(f'<b>➖ List of the files from ICS, 18th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_18.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_18.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/18/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 18th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_19', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/19'
    await call.message.answer(f'<b>➖ List of the files from ICS, 19th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_19.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_19.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/19/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 19th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_20', chat_id=moderators)
async def delete_files_ics_classes(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/20'
    await call.message.answer(f'<b>➖ List of the files from ICS, 20th week:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_20.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_20.file)
async def delete_files_ics_classes(message: types.Message, state: FSMContext):
    file_name = message.text
    try:
        path = f'/root/bot/media/ICS/20/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS, 20th week.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

@dp.callback_query_handler(text='delete_files_ics_books', chat_id=moderators)
async def delete_files_ics_books(call: types.CallbackQuery):
    path = '/root/bot/media/ICS/Books'
    await call.message.answer(f'<b>➖ List of the files from ICS books:</b>')
    for root, dirs, files in os.walk(path):
        for filename in files:
            await call.message.answer(filename)
        await call.message.answer('<b>➖ Enter a file name to delete:</b>')
        await delete_ics_books.file.set()

@dp.message_handler(IsPrivateMessage(), chat_id=moderators, state=delete_ics_books.file)
async def delete_files_ics_books(message: types.Message, state: FSMContext):
    file_name = message.text
    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    try:
        path = f'/root/bot/media/ICS/Books/{file_name}'
        os.remove(path)
        await message.answer(f'<b>➖ File "{file_name}" was deleted from ICS books.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>', reply_markup=ikb_delete_files_ics2)
        await state.finish()
    except FileNotFoundError:
        await message.answer('<b>⚠️ There is no such file.</b>')
        await message.answer('<b>➖ Deleting of the files:</b>'
                                     , reply_markup=ikb_delete_files_ics2)
        await state.finish()

# deleting files back
@dp.callback_query_handler(text='delete_files_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>📚 Editing of subjects files:</b>', reply_markup=ikb_files_manager)

@dp.callback_query_handler(text='delete_files_calculus_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_statistics_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_microeconomics_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_macroeconomics_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_history_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_philosophy_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_english_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)

@dp.callback_query_handler(text='delete_files_ics_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Deleting of the files:</b>', reply_markup=ikb_delete_files_subjects)





# ---------------- adding files
@dp.callback_query_handler(text='add_files', chat_id=moderators)
async def delete_files_command(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>'
                                 , reply_markup=ikb_files_subjects)

# adding files calculus
@dp.callback_query_handler(text='files_calculus', chat_id=moderators)
async def files_calculus(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_1', chat_id=moderators)
async def files_calculus_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 1st week:</b>')
    await calculus_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_1.file)
async def files_calculus_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 1st week.</b>')

    else:
        await message.answer('That is not a document.')
        await state.finish()

@dp.callback_query_handler(text='send_notification_calculus_1', chat_id=moderators, state=calculus_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_2', chat_id=moderators)
async def files_calculus_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 2nd week:</b>')
    await calculus_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_2.file)
async def files_calculus_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_2', chat_id=moderators, state=calculus_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_3', chat_id=moderators)
async def files_calculus_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 3rd week:</b>')
    await calculus_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_3.file)
async def files_calculus_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_3', chat_id=moderators, state=calculus_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_4', chat_id=moderators)
async def files_calculus_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 4th week:</b>')
    await calculus_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_4.file)
async def files_calculus_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_4', chat_id=moderators, state=calculus_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_5', chat_id=moderators)
async def files_calculus_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 5th week:</b>')
    await calculus_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_5.file)
async def files_calculus_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_5', chat_id=moderators, state=calculus_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_6', chat_id=moderators)
async def files_calculus_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 6th week:</b>')
    await calculus_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_6.file)
async def files_calculus_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_6', chat_id=moderators, state=calculus_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_7', chat_id=moderators)
async def files_calculus_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 7th week:</b>')
    await calculus_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_7.file)
async def files_calculus_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_7', chat_id=moderators, state=calculus_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_8', chat_id=moderators)
async def files_calculus_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 8th week:</b>')
    await calculus_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_8.file)
async def files_calculus_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_8', chat_id=moderators, state=calculus_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_9', chat_id=moderators)
async def files_calculus_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 9th week:</b>')
    await calculus_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_9.file)
async def files_calculus_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_9', chat_id=moderators, state=calculus_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_10', chat_id=moderators)
async def files_calculus_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 10th week:</b>')
    await calculus_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_10.file)
async def files_calculus_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_10', chat_id=moderators, state=calculus_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_11', chat_id=moderators)
async def files_calculus_11(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 11th week:</b>')
    await calculus_11.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_11.file)
async def files_calculus_11(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/11/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 11th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_11', chat_id=moderators, state=calculus_11.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 11 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_11.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_12', chat_id=moderators)
async def files_calculus_12(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 12th week:</b>')
    await calculus_12.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_12.file)
async def files_calculus_12(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/12/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 12th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_12', chat_id=moderators, state=calculus_12.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 12 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_12.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_13', chat_id=moderators)
async def files_calculus_13(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 13th week:</b>')
    await calculus_13.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_13.file)
async def files_calculus_13(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/13/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 13th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_13', chat_id=moderators, state=calculus_13.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 13 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_13.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_14', chat_id=moderators)
async def files_calculus_14(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 14th week:</b>')
    await calculus_14.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_14.file)
async def files_calculus_14(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/14/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 14th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_14', chat_id=moderators, state=calculus_14.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 14 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_14.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='files_calculus_15', chat_id=moderators)
async def files_calculus_15(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Calculus, 15th week:</b>')
    await calculus_15.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_15.file)
async def files_calculus_15(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/15/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 15th week.</b>')


@dp.callback_query_handler(text='send_notification_calculus_15', chat_id=moderators, state=calculus_15.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📘 Calculus, week 15 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_15.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

# @dp.callback_query_handler(text='files_calculus_16', chat_id=moderators)
# async def files_calculus_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Calculus, 16th week:</b>')
#     await calculus_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_16.file)
# async def files_calculus_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_calculus_16', chat_id=moderators, state=calculus_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='files_calculus_17', chat_id=moderators)
# async def files_calculus_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Calculus, 17th week:</b>')
#     await calculus_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_17.file)
# async def files_calculus_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_calculus_17', chat_id=moderators, state=calculus_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='files_calculus_18', chat_id=moderators)
# async def files_calculus_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Calculus, 18th week:</b>')
#     await calculus_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_18.file)
# async def files_calculus_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_calculus_18', chat_id=moderators, state=calculus_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='files_calculus_19', chat_id=moderators)
# async def files_calculus_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Calculus, 19th week:</b>')
#     await calculus_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_19.file)
# async def files_calculus_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_calculus_19', chat_id=moderators, state=calculus_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='files_calculus_20', chat_id=moderators)
# async def files_calculus_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Calculus, 20th week:</b>')
#     await calculus_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_20.file)
# async def files_calculus_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Calculus/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Calculus, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_calculus_20', chat_id=moderators, state=calculus_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📘 Calculus, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)
#
@dp.callback_query_handler(text='files_calculus_books', chat_id=moderators)
async def files_calculus_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in calculus books:</b>')
    await calculus_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=calculus_books.file)
async def files_calculus_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Calculus/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to calculus books.</b>')


@dp.callback_query_handler(text='send_notification_calculus_books', chat_id=moderators, state=calculus_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📘 Calculus books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=calculus_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_calculus2)

# adding files statistics
@dp.callback_query_handler(text='files_statistics', chat_id=moderators)
async def files_microeconomics(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_1', chat_id=moderators)
async def files_statistics_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 1st week:</b>')
    await statistics_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_1.file)
async def files_statistics_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to statistics, 1st week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_1', chat_id=moderators, state=statistics_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_2', chat_id=moderators)
async def files_statistics_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 2nd week:</b>')
    await statistics_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_2.file)
async def files_statistics_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_2', chat_id=moderators, state=statistics_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_3', chat_id=moderators)
async def files_statistics_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 3rd week:</b>')
    await statistics_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_3.file)
async def files_statistics_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_3', chat_id=moderators, state=statistics_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_4', chat_id=moderators)
async def files_statistics_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 4th week:</b>')
    await statistics_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_4.file)
async def files_statistics_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_4', chat_id=moderators, state=statistics_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_5', chat_id=moderators)
async def files_statistics_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 5th week:</b>')
    await statistics_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_5.file)
async def files_statistics_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_5', chat_id=moderators, state=statistics_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_6', chat_id=moderators)
async def files_statistics_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 6th week:</b>')
    await statistics_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_6.file)
async def files_statistics_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_6', chat_id=moderators, state=statistics_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_7', chat_id=moderators)
async def files_statistics_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 7th week:</b>')
    await statistics_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_7.file)
async def files_statistics_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_7', chat_id=moderators, state=statistics_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_8', chat_id=moderators)
async def files_statistics_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 8th week:</b>')
    await statistics_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_8.file)
async def files_statistics_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_8', chat_id=moderators, state=statistics_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_9', chat_id=moderators)
async def files_statistics_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 9th week:</b>')
    await statistics_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_9.file)
async def files_statistics_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_9', chat_id=moderators, state=statistics_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_10', chat_id=moderators)
async def files_statistics_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 10th week:</b>')
    await statistics_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_10.file)
async def files_statistics_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_10', chat_id=moderators, state=statistics_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_11', chat_id=moderators)
async def files_statistics_11(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Statistics, 11th week:</b>')
    await statistics_11.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_11.file)
async def files_statistics_11(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/11/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 11th week.</b>')


@dp.callback_query_handler(text='send_notification_statistics_11', chat_id=moderators, state=statistics_11.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📗 Statistics, week 11 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_11.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

# @dp.callback_query_handler(text='files_statistics_12', chat_id=moderators)
# async def files_statistics_12(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 12th week:</b>')
#     await statistics_12.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_12.file)
# async def files_statistics_12(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/12/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 12th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_12', chat_id=moderators, state=statistics_12.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_12.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_13', chat_id=moderators)
# async def files_statistics_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 13th week:</b>')
#     await statistics_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_13.file)
# async def files_statistics_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_13', chat_id=moderators, state=statistics_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_14', chat_id=moderators)
# async def files_statistics_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 14th week:</b>')
#     await statistics_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_14.file)
# async def files_statistics_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_14', chat_id=moderators, state=statistics_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_15', chat_id=moderators)
# async def files_statistics_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 15th week:</b>')
#     await statistics_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_15.file)
# async def files_statistics_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_15', chat_id=moderators, state=statistics_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_16', chat_id=moderators)
# async def files_statistics_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 16th week:</b>')
#     await statistics_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_16.file)
# async def files_statistics_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_16', chat_id=moderators, state=statistics_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_17', chat_id=moderators)
# async def files_statistics_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 17th week:</b>')
#     await statistics_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_17.file)
# async def files_statistics_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_17', chat_id=moderators, state=statistics_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_18', chat_id=moderators)
# async def files_statistics_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 18th week:</b>')
#     await statistics_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_18.file)
# async def files_statistics_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_18', chat_id=moderators, state=statistics_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_19', chat_id=moderators)
# async def files_statistics_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 19th week:</b>')
#     await statistics_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_19.file)
# async def files_statistics_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_19', chat_id=moderators, state=statistics_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='files_statistics_20', chat_id=moderators)
# async def files_statistics_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Statistics, 20th week:</b>')
#     await statistics_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_20.file)
# async def files_statistics_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Statistics/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Statistics, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_statistics_20', chat_id=moderators, state=statistics_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📗 Statistics, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='files_statistics_books', chat_id=moderators)
async def files_statistics_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in statistics books:</b>')
    await statistics_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=statistics_books.file)
async def files_statistics_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Statistics/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to statistics books.</b>')


@dp.callback_query_handler(text='send_notification_statistics_books', chat_id=moderators, state=statistics_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📗 Statistics books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=statistics_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_statistics2)

# adding files microeconomics
@dp.callback_query_handler(text='files_microeconomics', chat_id=moderators)
async def files_microeconomics(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_1', chat_id=moderators)
async def files_microeconomics_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 1st week:</b>')
    await microeconomics_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_1.file)
async def files_microeconomics_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 1st week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_1', chat_id=moderators, state=microeconomics_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_2', chat_id=moderators)
async def files_microeconomics_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 2nd week:</b>')
    await microeconomics_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_2.file)
async def files_microeconomics_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_2', chat_id=moderators, state=microeconomics_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_3', chat_id=moderators)
async def files_microeconomics_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 3rd week:</b>')
    await microeconomics_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_3.file)
async def files_microeconomics_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_3', chat_id=moderators, state=microeconomics_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_4', chat_id=moderators)
async def files_microeconomics_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 4th week:</b>')
    await microeconomics_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_4.file)
async def files_microeconomics_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_4', chat_id=moderators, state=microeconomics_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_5', chat_id=moderators)
async def files_microeconomics_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 5th week:</b>')
    await microeconomics_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_5.file)
async def files_microeconomics_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_5', chat_id=moderators, state=microeconomics_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_6', chat_id=moderators)
async def files_microeconomics_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 6th week:</b>')
    await microeconomics_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_6.file)
async def files_microeconomics_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_6', chat_id=moderators, state=microeconomics_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_7', chat_id=moderators)
async def files_microeconomics_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 7th week:</b>')
    await microeconomics_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_7.file)
async def files_microeconomics_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_7', chat_id=moderators, state=microeconomics_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_8', chat_id=moderators)
async def files_microeconomics_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 8th week:</b>')
    await microeconomics_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_8.file)
async def files_microeconomics_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_8', chat_id=moderators, state=microeconomics_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_9', chat_id=moderators)
async def files_microeconomics_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 9th week:</b>')
    await microeconomics_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_9.file)
async def files_microeconomics_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_9', chat_id=moderators, state=microeconomics_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_10', chat_id=moderators)
async def files_microeconomics_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 10th week:</b>')
    await microeconomics_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_10.file)
async def files_microeconomics_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_10', chat_id=moderators, state=microeconomics_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_11', chat_id=moderators)
async def files_microeconomics_11(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Microeconomics, 11th week:</b>')
    await microeconomics_11.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_11.file)
async def files_microeconomics_11(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/11/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 11th week.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_11', chat_id=moderators, state=microeconomics_11.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📙 Microeconomics, week 11 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_11.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

# @dp.callback_query_handler(text='files_microeconomics_12', chat_id=moderators)
# async def files_microeconomics_12(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 12th week:</b>')
#     await microeconomics_12.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_12.file)
# async def files_microeconomics_12(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/12/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 12th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_12', chat_id=moderators, state=microeconomics_12.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_12.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_13', chat_id=moderators)
# async def files_microeconomics_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 13th week:</b>')
#     await microeconomics_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_13.file)
# async def files_microeconomics_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_13', chat_id=moderators, state=microeconomics_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_14', chat_id=moderators)
# async def files_microeconomics_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 14th week:</b>')
#     await microeconomics_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_14.file)
# async def files_microeconomics_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_14', chat_id=moderators, state=microeconomics_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_15', chat_id=moderators)
# async def files_microeconomics_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 15th week:</b>')
#     await microeconomics_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_15.file)
# async def files_microeconomics_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_15', chat_id=moderators, state=microeconomics_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_16', chat_id=moderators)
# async def files_microeconomics_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 16th week:</b>')
#     await microeconomics_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_16.file)
# async def files_microeconomics_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_16', chat_id=moderators, state=microeconomics_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_17', chat_id=moderators)
# async def files_microeconomics_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 17th week:</b>')
#     await microeconomics_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_17.file)
# async def files_microeconomics_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_17', chat_id=moderators, state=microeconomics_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_18', chat_id=moderators)
# async def files_microeconomics_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 18th week:</b>')
#     await microeconomics_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_18.file)
# async def files_microeconomics_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_18', chat_id=moderators, state=microeconomics_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_19', chat_id=moderators)
# async def files_microeconomics_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 19th week:</b>')
#     await microeconomics_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_19.file)
# async def files_microeconomics_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_19', chat_id=moderators, state=microeconomics_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='files_microeconomics_20', chat_id=moderators)
# async def files_microeconomics_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Microeconomics, 20th week:</b>')
#     await microeconomics_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_20.file)
# async def files_microeconomics_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Microeconomics/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Microeconomics, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_microeconomics_20', chat_id=moderators, state=microeconomics_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📙 Microeconomics, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='files_microeconomics_books', chat_id=moderators)
async def files_microeconomics_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in microeconomics books:</b>')
    await microeconomics_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=microeconomics_books.file)
async def files_microeconomics_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Microeconomics/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to microeconomics books.</b>')


@dp.callback_query_handler(text='send_notification_microeconomics_books', chat_id=moderators, state=microeconomics_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📙 Microeconomics books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=microeconomics_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_microeconomics2)

# adding files macroeconomics
# @dp.callback_query_handler(text='files_macroeconomics', chat_id=moderators)
# async def files_macroeconomics(call: types.CallbackQuery):
#     await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
#                                  , reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_1', chat_id=moderators)
# async def files_macroeconomics_1(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 1st week:</b>')
#     await macroeconomics_1.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_1.file)
# async def files_macroeconomics_1(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/1/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 1st week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_1', chat_id=moderators, state=macroeconomics_1.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_1.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_2', chat_id=moderators)
# async def files_macroeconomics_2(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 2nd week:</b>')
#     await macroeconomics_2.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_2.file)
# async def files_macroeconomics_2(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/2/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 2nd week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_2', chat_id=moderators, state=macroeconomics_2.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_2.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_3', chat_id=moderators)
# async def files_macroeconomics_3(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 3rd week:</b>')
#     await macroeconomics_3.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_3.file)
# async def files_macroeconomics_3(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/3/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 3rd week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_3', chat_id=moderators, state=macroeconomics_3.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_3.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_4', chat_id=moderators)
# async def files_macroeconomics_4(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 4th week:</b>')
#     await macroeconomics_4.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_4.file)
# async def files_macroeconomics_4(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/4/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 4th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_4', chat_id=moderators, state=macroeconomics_4.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_4.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_5', chat_id=moderators)
# async def files_macroeconomics_5(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 5th week:</b>')
#     await macroeconomics_5.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_5.file)
# async def files_macroeconomics_5(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/5/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 5th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_5', chat_id=moderators, state=macroeconomics_5.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_5.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_6', chat_id=moderators)
# async def files_macroeconomics_6(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 6th week:</b>')
#     await macroeconomics_6.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_6.file)
# async def files_macroeconomics_6(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/6/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 6th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_6', chat_id=moderators, state=macroeconomics_6.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_6.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_7', chat_id=moderators)
# async def files_macroeconomics_7(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 7th week:</b>')
#     await macroeconomics_7.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_7.file)
# async def files_macroeconomics_7(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/7/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 7th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_7', chat_id=moderators, state=macroeconomics_7.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_7.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_8', chat_id=moderators)
# async def files_macroeconomics_8(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 8th week:</b>')
#     await macroeconomics_8.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_8.file)
# async def files_macroeconomics_8(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/8/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 8th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_8', chat_id=moderators, state=macroeconomics_8.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_8.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_9', chat_id=moderators)
# async def files_macroeconomics_9(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 9th week:</b>')
#     await macroeconomics_9.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_9.file)
# async def files_macroeconomics_9(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/9/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 9th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_9', chat_id=moderators, state=macroeconomics_9.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_9.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_10', chat_id=moderators)
# async def files_macroeconomics_10(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 10th week:</b>')
#     await macroeconomics_10.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_10.file)
# async def files_macroeconomics_10(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/10/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 10th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_10', chat_id=moderators, state=macroeconomics_10.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_10.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_11', chat_id=moderators)
# async def files_macroeconomics_11(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 11th week:</b>')
#     await macroeconomics_11.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_11.file)
# async def files_macroeconomics_11(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/11/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 11th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_11', chat_id=moderators, state=macroeconomics_11.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_11.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_12', chat_id=moderators)
# async def files_macroeconomics_12(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 12th week:</b>')
#     await macroeconomics_12.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_12.file)
# async def files_macroeconomics_12(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/12/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 12th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_12', chat_id=moderators, state=macroeconomics_12.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_12.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_13', chat_id=moderators)
# async def files_macroeconomics_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 13th week:</b>')
#     await macroeconomics_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_13.file)
# async def files_macroeconomics_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_13', chat_id=moderators, state=macroeconomics_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_14', chat_id=moderators)
# async def files_macroeconomics_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 14th week:</b>')
#     await macroeconomics_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_14.file)
# async def files_macroeconomics_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_14', chat_id=moderators, state=macroeconomics_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_15', chat_id=moderators)
# async def files_macroeconomics_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 15th week:</b>')
#     await macroeconomics_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_15.file)
# async def files_macroeconomics_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_15', chat_id=moderators, state=macroeconomics_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_16', chat_id=moderators)
# async def files_macroeconomics_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 16th week:</b>')
#     await macroeconomics_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_16.file)
# async def files_macroeconomics_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_16', chat_id=moderators, state=macroeconomics_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_17', chat_id=moderators)
# async def files_macroeconomics_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 17th week:</b>')
#     await macroeconomics_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_17.file)
# async def files_macroeconomics_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_17', chat_id=moderators, state=macroeconomics_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_18', chat_id=moderators)
# async def files_macroeconomics_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 18th week:</b>')
#     await macroeconomics_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_18.file)
# async def files_macroeconomics_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_18', chat_id=moderators, state=macroeconomics_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_19', chat_id=moderators)
# async def files_macroeconomics_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 19th week:</b>')
#     await macroeconomics_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_19.file)
# async def files_macroeconomics_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_19', chat_id=moderators, state=macroeconomics_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='files_macroeconomics_20', chat_id=moderators)
# async def files_macroeconomics_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Macroeconomics, 20th week:</b>')
#     await macroeconomics_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=macroeconomics_20.file)
# async def files_macroeconomics_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Macroeconomics/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Macroeconomics, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_macroeconomics_20', chat_id=moderators, state=macroeconomics_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📕 Macroeconomics, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
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
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to macroeconomics books.</b>')

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
#         if user.notification_status == 'On':
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         else:
#             pass
#     await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=macroeconomics_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_macroeconomics2)

# adding files history
@dp.callback_query_handler(text='files_history', chat_id=moderators)
async def files_history(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_1', chat_id=moderators)
async def files_history_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 1st week:</b>')
    await history_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_1.file)
async def files_history_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 1st week.</b>')


@dp.callback_query_handler(text='send_notification_history_1', chat_id=moderators, state=history_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_2', chat_id=moderators)
async def files_history_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 2nd week:</b>')
    await history_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_2.file)
async def files_history_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_history_2', chat_id=moderators, state=history_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_3', chat_id=moderators)
async def files_history_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 3rd week:</b>')
    await history_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_3.file)
async def files_history_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_history_3', chat_id=moderators, state=history_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_4', chat_id=moderators)
async def files_history_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 4th week:</b>')
    await history_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_4.file)
async def files_history_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_history_4', chat_id=moderators, state=history_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_5', chat_id=moderators)
async def files_history_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 5th week:</b>')
    await history_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_5.file)
async def files_history_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_history_5', chat_id=moderators, state=history_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_6', chat_id=moderators)
async def files_history_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 6th week:</b>')
    await history_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_6.file)
async def files_history_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_history_6', chat_id=moderators, state=history_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_7', chat_id=moderators)
async def files_history_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 7th week:</b>')
    await history_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_7.file)
async def files_history_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_history_7', chat_id=moderators, state=history_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_8', chat_id=moderators)
async def files_history_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 8th week:</b>')
    await history_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_8.file)
async def files_history_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_history_8', chat_id=moderators, state=history_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_9', chat_id=moderators)
async def files_history_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 9th week:</b>')
    await history_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_9.file)
async def files_history_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_history_9', chat_id=moderators, state=history_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_10', chat_id=moderators)
async def files_history_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 10th week:</b>')
    await history_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_10.file)
async def files_history_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_history_10', chat_id=moderators, state=history_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_11', chat_id=moderators)
async def files_history_11(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 11th week:</b>')
    await history_11.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_11.file)
async def files_history_11(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/11/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 11th week.</b>')


@dp.callback_query_handler(text='send_notification_history_11', chat_id=moderators, state=history_11.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 11 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_11.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_12', chat_id=moderators)
async def files_history_12(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in History, 12th week:</b>')
    await history_12.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_12.file)
async def files_history_12(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/12/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 12th week.</b>')


@dp.callback_query_handler(text='send_notification_history_12', chat_id=moderators, state=history_12.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📔 History, week 12 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_12.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

# @dp.callback_query_handler(text='files_history_13', chat_id=moderators)
# async def files_history_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 13th week:</b>')
#     await history_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_13.file)
# async def files_history_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_13', chat_id=moderators, state=history_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_14', chat_id=moderators)
# async def files_history_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 14th week:</b>')
#     await history_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_14.file)
# async def files_history_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_14', chat_id=moderators, state=history_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_15', chat_id=moderators)
# async def files_history_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 15th week:</b>')
#     await history_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_15.file)
# async def files_history_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_15', chat_id=moderators, state=history_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_16', chat_id=moderators)
# async def files_history_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 16th week:</b>')
#     await history_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_16.file)
# async def files_history_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_16', chat_id=moderators, state=history_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_17', chat_id=moderators)
# async def files_history_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 17th week:</b>')
#     await history_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_17.file)
# async def files_history_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_17', chat_id=moderators, state=history_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_18', chat_id=moderators)
# async def files_history_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 18th week:</b>')
#     await history_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_18.file)
# async def files_history_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_18', chat_id=moderators, state=history_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_19', chat_id=moderators)
# async def files_history_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 19th week:</b>')
#     await history_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_19.file)
# async def files_history_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_19', chat_id=moderators, state=history_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='files_history_20', chat_id=moderators)
# async def files_history_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in History, 20th week:</b>')
#     await history_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=history_20.file)
# async def files_history_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/History/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to History, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_history_20', chat_id=moderators, state=history_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📔 History, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='files_history_books', chat_id=moderators)
async def files_history_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in history books:</b>')
    await history_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=history_books.file)
async def files_history_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/History/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to history books.</b>')


@dp.callback_query_handler(text='send_notification_history_books', chat_id=moderators, state=history_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📔 History books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=history_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_history2)

# adding files Philosophy
@dp.callback_query_handler(text='files_philosophy', chat_id=moderators)
async def files_philosophy(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_1', chat_id=moderators)
async def files_philosophy_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 1st week:</b>')
    await philosophy_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_1.file)
async def files_philosophy_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 1st week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_1', chat_id=moderators, state=philosophy_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_2', chat_id=moderators)
async def files_philosophy_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 2nd week:</b>')
    await philosophy_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_2.file)
async def files_philosophy_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_2', chat_id=moderators, state=philosophy_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_3', chat_id=moderators)
async def files_philosophy_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 3rd week:</b>')
    await philosophy_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_3.file)
async def files_philosophy_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_3', chat_id=moderators, state=philosophy_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_4', chat_id=moderators)
async def files_philosophy_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 4th week:</b>')
    await philosophy_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_4.file)
async def files_philosophy_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_4', chat_id=moderators, state=philosophy_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_5', chat_id=moderators)
async def files_philosophy_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 5th week:</b>')
    await philosophy_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_5.file)
async def files_philosophy_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_5', chat_id=moderators, state=philosophy_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_6', chat_id=moderators)
async def files_philosophy_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 6th week:</b>')
    await philosophy_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_6.file)
async def files_philosophy_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_6', chat_id=moderators, state=philosophy_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_7', chat_id=moderators)
async def files_philosophy_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 7th week:</b>')
    await philosophy_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_7.file)
async def files_philosophy_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_7', chat_id=moderators, state=philosophy_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_8', chat_id=moderators)
async def files_philosophy_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 8th week:</b>')
    await philosophy_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_8.file)
async def files_philosophy_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_8', chat_id=moderators, state=philosophy_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_9', chat_id=moderators)
async def files_philosophy_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 9th week:</b>')
    await philosophy_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_9.file)
async def files_philosophy_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_9', chat_id=moderators, state=philosophy_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_10', chat_id=moderators)
async def files_philosophy_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 10th week:</b>')
    await philosophy_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_10.file)
async def files_philosophy_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_10', chat_id=moderators, state=philosophy_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_11', chat_id=moderators)
async def files_philosophy_11(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 11th week:</b>')
    await philosophy_11.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_11.file)
async def files_philosophy_11(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/11/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 11th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_11', chat_id=moderators, state=philosophy_11.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 11 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_11.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_12', chat_id=moderators)
async def files_philosophy_12(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in Philosophy, 12th week:</b>')
    await philosophy_12.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_12.file)
async def files_philosophy_12(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/12/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 12th week.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_12', chat_id=moderators, state=philosophy_12.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📒 Philosophy, week 12 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_12.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

# @dp.callback_query_handler(text='files_philosophy_13', chat_id=moderators)
# async def files_philosophy_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 13th week:</b>')
#     await philosophy_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_13.file)
# async def files_philosophy_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_13', chat_id=moderators, state=philosophy_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_14', chat_id=moderators)
# async def files_philosophy_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 14th week:</b>')
#     await philosophy_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_14.file)
# async def files_philosophy_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_14', chat_id=moderators, state=philosophy_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_15', chat_id=moderators)
# async def files_philosophy_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 15th week:</b>')
#     await philosophy_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_15.file)
# async def files_philosophy_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_15', chat_id=moderators, state=philosophy_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_16', chat_id=moderators)
# async def files_philosophy_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 16th week:</b>')
#     await philosophy_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_16.file)
# async def files_philosophy_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_16', chat_id=moderators, state=philosophy_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_17', chat_id=moderators)
# async def files_philosophy_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 17th week:</b>')
#     await philosophy_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_17.file)
# async def files_philosophy_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_17', chat_id=moderators, state=philosophy_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_18', chat_id=moderators)
# async def files_philosophy_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 18th week:</b>')
#     await philosophy_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_18.file)
# async def files_philosophy_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_18', chat_id=moderators, state=philosophy_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_19', chat_id=moderators)
# async def files_philosophy_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 19th week:</b>')
#     await philosophy_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_19.file)
# async def files_philosophy_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_19', chat_id=moderators, state=philosophy_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='files_philosophy_20', chat_id=moderators)
# async def files_philosophy_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in Philosophy, 20th week:</b>')
#     await philosophy_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_20.file)
# async def files_philosophy_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/Philosophy/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to Philosophy, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_philosophy_20', chat_id=moderators, state=philosophy_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📒 Philosophy, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='files_philosophy_books', chat_id=moderators)
async def files_philosophy_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in philosophy books:</b>')
    await philosophy_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=philosophy_books.file)
async def files_philosophy_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/Philosophy/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to philosophy books.</b>')


@dp.callback_query_handler(text='send_notification_philosophy_books', chat_id=moderators, state=philosophy_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📒 Philosophy books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=philosophy_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_philosophy2)

# adding files english
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
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to english classes.</b>')

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
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_classes.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
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
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to english homework.</b>')

#
# @dp.callback_query_handler(text='send_notification_english_homework', chat_id=moderators, state=english_homework.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>🇬🇧 English homework has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_homework.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
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
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to english books.</b>')

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
#         if user.notification_status == 'On':
#             try:
#                 await dp.bot.send_message(chat_id=user.user_id, text=text)
#             except Exception:
#                 pass
#         else:
#             pass
#     await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=english_books.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_english)
#
# adding files ICS
@dp.callback_query_handler(text='files_ics', chat_id=moderators)
async def files_microeconomics(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>\n\n'
                                 , reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_1', chat_id=moderators)
async def files_ics_1(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 1st week:</b>')
    await ics_1.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_1.file)
async def files_ics_1(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/1/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 1st week.</b>')


@dp.callback_query_handler(text='send_notification_ics_1', chat_id=moderators, state=ics_1.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 1 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_1.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_2', chat_id=moderators)
async def files_ics_2(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 2nd week:</b>')
    await ics_2.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_2.file)
async def files_ics_2(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/2/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 2nd week.</b>')


@dp.callback_query_handler(text='send_notification_ics_2', chat_id=moderators, state=ics_2.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 2 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_2.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_3', chat_id=moderators)
async def files_ics_3(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 3rd week:</b>')
    await ics_3.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_3.file)
async def files_ics_3(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/3/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 3rd week.</b>')


@dp.callback_query_handler(text='send_notification_ics_3', chat_id=moderators, state=ics_3.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 3 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_3.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_4', chat_id=moderators)
async def files_ics_4(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 4th week:</b>')
    await ics_4.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_4.file)
async def files_ics_4(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/4/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 4th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_4', chat_id=moderators, state=ics_4.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 4 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_4.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_5', chat_id=moderators)
async def files_ics_5(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 5th week:</b>')
    await ics_5.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_5.file)
async def files_ics_5(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/5/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 5th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_5', chat_id=moderators, state=ics_5.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 5 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_5.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_6', chat_id=moderators)
async def files_ics_6(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 6th week:</b>')
    await ics_6.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_6.file)
async def files_ics_6(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/6/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 6th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_6', chat_id=moderators, state=ics_6.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 6 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_6.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_7', chat_id=moderators)
async def files_ics_7(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 7th week:</b>')
    await ics_7.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_7.file)
async def files_ics_7(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/7/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 7th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_7', chat_id=moderators, state=ics_7.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 7 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_7.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_8', chat_id=moderators)
async def files_ics_8(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 8th week:</b>')
    await ics_8.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_8.file)
async def files_ics_8(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/8/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 8th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_8', chat_id=moderators, state=ics_8.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 8 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_8.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_9', chat_id=moderators)
async def files_ics_9(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 9th week:</b>')
    await ics_9.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_9.file)
async def files_ics_9(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/9/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 9th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_9', chat_id=moderators, state=ics_9.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 9 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_9.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_10', chat_id=moderators)
async def files_ics_10(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS, 10th week:</b>')
    await ics_10.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_10.file)
async def files_ics_10(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/10/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 10th week.</b>')


@dp.callback_query_handler(text='send_notification_ics_10', chat_id=moderators, state=ics_10.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
        users = await quick_commands.select_all_users()
        data = await state.get_data()
        file_name = data.get('file_name')
        text = f'<b>📓 ICS, week 10 has been updated.</b>\n\n' \
               f'<b>Added file:</b> {file_name}'
        await state.finish()
        await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_10.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

# @dp.callback_query_handler(text='files_ics_11', chat_id=moderators)
# async def files_ics_11(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 11th week:</b>')
#     await ics_11.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_11.file)
# async def files_ics_11(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/11/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 11th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_11', chat_id=moderators, state=ics_11.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_11.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_12', chat_id=moderators)
# async def files_ics_12(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 12th week:</b>')
#     await ics_12.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_12.file)
# async def files_ics_12(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/12/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 12th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_12', chat_id=moderators, state=ics_12.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_12.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_13', chat_id=moderators)
# async def files_ics_13(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 13th week:</b>')
#     await ics_13.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_13.file)
# async def files_ics_13(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/13/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 13th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_13', chat_id=moderators, state=ics_13.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_13.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_14', chat_id=moderators)
# async def files_ics_14(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 14th week:</b>')
#     await ics_14.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_14.file)
# async def files_ics_14(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/14/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 14th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_14', chat_id=moderators, state=ics_14.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_14.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_15', chat_id=moderators)
# async def files_ics_15(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 15th week:</b>')
#     await ics_15.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_15.file)
# async def files_ics_15(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/15/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 15th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_15', chat_id=moderators, state=ics_15.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_15.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_16', chat_id=moderators)
# async def files_ics_16(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 16th week:</b>')
#     await ics_16.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_16.file)
# async def files_ics_16(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/16/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 16th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_16', chat_id=moderators, state=ics_16.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_16.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_17', chat_id=moderators)
# async def files_ics_17(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 17th week:</b>')
#     await ics_17.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_17.file)
# async def files_ics_17(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/17/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 17th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_17', chat_id=moderators, state=ics_17.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_17.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_18', chat_id=moderators)
# async def files_ics_18(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 18th week:</b>')
#     await ics_18.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_18.file)
# async def files_ics_18(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/18/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 18th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_18', chat_id=moderators, state=ics_18.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_18.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_19', chat_id=moderators)
# async def files_ics_19(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 19th week:</b>')
#     await ics_19.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_19.file)
# async def files_ics_19(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/19/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 19th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_19', chat_id=moderators, state=ics_19.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 1week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_19.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='files_ics_20', chat_id=moderators)
# async def files_ics_20(call: types.CallbackQuery):
#     await call.message.answer('<b>➕ Send a file to add in ICS, 20th week:</b>')
#     await ics_20.file.set()
#
# @dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_20.file)
# async def files_ics_20(message: types.Message, state: FSMContext):
#     file_name = message.document.file_name
#     await state.update_data(file_name=file_name)
#     if document := message.document:
#         await document.download(
#             destination_file=f'media/ICS/20/{file_name}'
#         )
#         await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS, 20th week.</b>')

#
# @dp.callback_query_handler(text='send_notification_ics_20', chat_id=moderators, state=ics_20.file)
# async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
#         users = await quick_commands.select_all_users()
#         data = await state.get_data()
#         file_name = data.get('file_name')
#         text = f'<b>📓 ICS, 2week has been updated.</b>\n\n' \
#                f'<b>Added file:</b> {file_name}'
#         await state.finish()
#         for user in users:
#             if user.notification_status == 'On':
#                 try:
#                     await dp.bot.send_message(chat_id=user.user_id, text=text)
#                 except Exception:
#                     pass
#             else:
#                 pass
#         await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
#         await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)
#
# @dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_20.file)
# async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
#     await state.finish()
#     await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
#     await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='files_ics_books', chat_id=moderators)
async def files_ics_books(call: types.CallbackQuery):
    await call.message.answer('<b>➕ Send a file to add in ICS books:</b>')
    await ics_books.file.set()

@dp.message_handler(content_types=['document'], chat_id=moderators, state=ics_books.file)
async def files_ics_homework(message: types.Message, state: FSMContext):
    file_name = message.document.file_name
    await state.update_data(file_name=file_name)
    if document := message.document:
        await document.download(
            destination_file=f'media/ICS/Books/{file_name}'
        )
        await message.answer(f'<b>➕ File "{file_name}" <ins>has been added</ins> to ICS books.</b>')


@dp.callback_query_handler(text='send_notification_ics_books', chat_id=moderators, state=ics_books.file)
async def files_send_notification(call: types.CallbackQuery, state: FSMContext):
    users = await quick_commands.select_all_users()
    data = await state.get_data()
    file_name = data.get('file_name')
    text = f'<b>📓 ICS books were updated.</b>\n\n' \
           f'<b>Added file:</b> {file_name}'
    await state.finish()
    for user in users:
        if user.notification_status == 'On':
            try:
                await dp.bot.send_message(chat_id=user.user_id, text=text)
            except Exception:
                pass
        else:
            pass
    await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

@dp.callback_query_handler(text='cancel_notification', chat_id=moderators, state=ics_books.file)
async def files_cancel_notification(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>🔇 Notification <ins>has been canceled</ins>.</b>')
    await call.message.answer('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_ics2)

# adding files back
@dp.callback_query_handler(text='adding_files_back', chat_id=moderators)
async def files_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>📚 Editing of subjects files:</b>', reply_markup=ikb_files_manager)

@dp.callback_query_handler(text='files_calculus_back', chat_id=moderators)
async def files_calculus_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_statistics_back', chat_id=moderators)
async def files_statistics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_microeconomics_back', chat_id=moderators)
async def files_microeconomics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_macroeconomics_back', chat_id=moderators)
async def files_macroeconomics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_history_back', chat_id=moderators)
async def files_ics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_philosophy_back', chat_id=moderators)
async def files_ics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_english_back', chat_id=moderators)
async def files_english_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)

@dp.callback_query_handler(text='files_ics_back', chat_id=moderators)
async def files_ics_cancel(call: types.CallbackQuery):
    await call.message.edit_text('<b>➕ Adding of the files:</b>', reply_markup=ikb_files_subjects)


# for user in users:
#     if user.notification_status == 'On':
#         try:
#             await dp.bot.send_message(chat_id=user.user_id, text=text)
#         except Exception:
#             pass
#     else:
#         pass
# await call.message.edit_text('<b>🔊 Notification <ins>has been sent</ins>.</b>')
