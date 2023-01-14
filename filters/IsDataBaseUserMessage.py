from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Message, CallbackQuery

from keyboards.inline.inline_keyboard_registration import ikb_registration
from utils.db_api import quick_commands as commands



class IsDatabaseUserMessage(BoundFilter):
    async def check(self, message: Message) -> bool:
        user = await commands.select_user(message.from_user.id)
        if user:
            return True
        else:
            # await message.answer("⚠️ It's private - only for ICEF students. To get an access, contact with @paoloppv.")
            await message.answer("<b>🌐 You're not registered.</b>\n\n"
                                 'Click the button below to register and enter to the bot. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_registration)
            raise CancelHandler()

class IsDatabaseUserCallback(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        user = await commands.select_user(call.from_user.id)
        if user:
            return True
        else:
            # await call.message.answer('<b>🌐 Welcome to <ins>ICEF Helper</ins>.</b>\n\n'
            #                      '⚠️ The bot is private. Only for ICEF students. To get an access, contact with @paoloppv.')
            await call.message.answer("<b>🌐 You're not registered.</b>\n\n"
                                 'Click the button below to register and enter to the bot. <a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_registration)
            raise CancelHandler()


