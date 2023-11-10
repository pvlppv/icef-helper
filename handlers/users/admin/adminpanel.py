from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_settings import ikb_settings_admins
from loader import dp

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='/admin')
async def admin_panel(message: types.Message):
    await message.answer(f'<b>👨🏼‍💻 Admin Panel:</b>', reply_markup=ikb_settings_admins)

@dp.callback_query_handler(text='admin_panel_back')
async def admin_panel_back(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>👨🏼‍💻 Admin Panel:</b>', reply_markup=ikb_settings_admins)

