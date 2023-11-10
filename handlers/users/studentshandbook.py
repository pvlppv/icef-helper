from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.default import kb_handbook
from keyboards.inline.inline_keyboard_handbook import ikb_handbook
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='🗃 Handbook')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🗃 Handbook')
async def command_handbook(message: types.Message):
    await message.answer(f'<b>🗃 Handbook:</b> <a href="https://telegra.ph/file/2d25d1591b5c1bd50dce2.png">ㅤ</a>', reply_markup=ikb_handbook)