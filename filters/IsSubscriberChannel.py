from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.keyboard_ICEFHelper import kb_ICEFHelperMenu
from keyboards.inline.inline_keyboard_homepage import ikb_homepage
from loader import dp, bot

Channels = [
    ['ICEF Helper Channel', '-1001558263757', 'https://t.me/+DFuYOJt5rcpjMWZi']
]

# async def check_sub_channels(channels, user_id):
#     for channel in channels:
#         chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
#         if chat_member['status'] == 'left':
#             return False
#     return True

markup = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='ICEF Helper Channel', url='https://t.me/+DFuYOJt5rcpjMWZi'),
                                  ],
                                  [
                                      InlineKeyboardButton(text='✅ Subscribed', callback_data='subscribed'),
                                  ]
                              ])

@dp.callback_query_handler(text='subscribed')
async def subscribed(call: types.CallbackQuery):
    chat_member = await bot.get_chat_member(chat_id='-1001558263757', user_id=call.from_user.id)
    if chat_member['status'] == 'left':
        await call.answer("You're not subscribed.", show_alert=True)
    else:
        await dp.bot.delete_message(call.from_user.id, call.message.message_id)
        await call.answer('Thank you.', show_alert=True)
        await dp.bot.send_message(call.from_user.id, f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_homepage)

class IsSubscriberChannelMessage(BoundFilter):
    async def check(self, message: Message) -> bool:
        chat_member = await bot.get_chat_member(chat_id='-1001558263757', user_id=message.from_user.id)
        if chat_member['status'] == 'left':
            await message.answer("🌐 Subscribe to the bot's channel to check all latest news and updates: https://t.me/+DFuYOJt5rcpjMWZi.", reply_markup=markup)
            raise CancelHandler()
        else:
            return True

class IsSubscriberChannelCallback(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        chat_member = await bot.get_chat_member(chat_id='-1001558263757', user_id=call.from_user.id)
        if chat_member['status'] == 'left':
            await call.message.answer("🌐 Subscribe to the bot's channel to check all latest news and updates: https://t.me/+DFuYOJt5rcpjMWZi.", reply_markup=markup)
            raise CancelHandler()
        else:
            return True

