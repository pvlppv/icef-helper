from aiogram.types import CallbackQuery

from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from filters.IsDataBaseUserMessage import IsDatabaseUserCallback
from keyboards.default import kb_menu
from keyboards.inline import ikb_menu
from loader import dp
from aiogram import types
from utils.misc import rate_limit

@rate_limit(limit=3, key='/materials')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/materials')
async def show_inline_menu(message: types.Message):
    await message.answer(f'<b>📂 Useful materials:</b>', reply_markup=ikb_menu)

#@dp.callback_query_handler(text='Books')
#async def send_message(call: CallbackQuery):
#    await call.message.answer('Books:\n\n'
#                              'https://drive.google.com/drive/folders/1JqfU-xubOSG-9RdEBWlwnSbWWTZABpm7')
#
#@dp.callback_query_handler(text='Past exams')
#async def send_message(call: CallbackQuery):
#    await call.message.answer('ICEF past exams:\n\n'
#                              'https://drive.google.com/drive/folders/1AA3FPxFm7jOKJFN2mAi3fjiPR0ZgAbhG')
#
#@dp.callback_query_handler(text='Custom content')
#async def send_message(call: CallbackQuery):
#    await call.message.answer('Custom content:\n\n'
#                              'https://drive.google.com/drive/folders/1m-9D5vGWsR7ydgVCO1qFCBig9084MmLC')
#
#@dp.callback_query_handler(text='Career materials')
#async def send_message(call: CallbackQuery):
#    await call.message.answer('Career materials:\n\n'
#                              'https://drive.google.com/drive/folders/1HeMXUe0HHl-WdS4BqX6dJAyJOBbGP2t1')
#
#@dp.callback_query_handler(text='UoL')
#async def send_message(call: CallbackQuery):
#    await call.message.answer('UoL 2003-2017:\n\n'
#                              'https://drive.google.com/drive/folders/1sML4jKYIWvxf8gk0a-D5mtToDjykZWOj')








# плашечка сверху
# @dp.callback_query_handler(text='Past exams')
# async def send_message(call: CallbackQuery):
#     await call.answer('ICEF past exams:')

# уведомление выскакивающее
# @dp.callback_query_handler(text='Name')
# async def send_message(call: CallbackQuery):
#     await call.answer('POKROVKA', show_alert=True)



# @dp.callback_query_handler(text='New menu')
# async def send_message(call: CallbackQuery):
#     await call.message.answer('New menu!', reply_markup=ikb_menu2)

# @dp.callback_query_handler(text='New menu2')
# async def send_message(call: CallbackQuery):
#     await call.message.edit_reply_markup(ikb_menu2)

# @dp.callback_query_handler(text='⬅️ Back')
# async def send_message(call: CallbackQuery):
#     await call.message.edit_reply_markup(ikb_menu)

