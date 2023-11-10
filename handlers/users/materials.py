from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline import ikb_materials
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='📂 Materials')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📂 Materials')
async def command_materials(message: types.Message):
    await message.answer(f'<b>📂 Materials:</b> <a href="https://telegra.ph/file/144d9df6cf5c4e10a3459.png">ㅤ</a>', reply_markup=ikb_materials)


# плашечка сверху
# @dp.callback_query_handler(text='Past exams')
# async def send_message(call: CallbackQuery):
#     await call.answer('ICEF past exams:')

# уведомление выскакивающее
# @dp.callback_query_handler(text='Name')
# async def send_message(call: CallbackQuery):
#     await call.answer('POKROVKA', show_alert=True)

