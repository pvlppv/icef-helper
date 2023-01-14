from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Message, CallbackQuery

from keyboards.inline.inline_keyboard_registration import ikb_registration
from utils.db_api import quick_commands as commands



class IsAcceptedUserMessage(BoundFilter):
    async def check(self, message: Message) -> bool:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'Accepted':
            return True
        else:
            # await message.answer("⚠️ It's private - only for ICEF students. To get an access, contact with @paoloppv.")
            await message.answer("<b>🌐 Your registration is still on a check.</b>\n\n")
            raise CancelHandler()


class IsAccepterUserCallback(BoundFilter):
    async def check(self, call: CallbackQuery) -> bool:
        user = await commands.select_user(call.from_user.id)
        if user.status == 'Accepted':
            return True
        else:
            # await call.message.answer('<b>🌐 Welcome to <ins>ICEF Helper</ins>.</b>\n\n'
            #                      '⚠️ The bot is private. Only for ICEF students. To get an access, contact with @paoloppv.')
            await call.message.answer("<b>🌐 Your registration is still on a check.</b>\n\n")
            raise CancelHandler()


