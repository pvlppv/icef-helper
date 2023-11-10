from aiogram import types

from filters import IsPrivateMessage
from loader import dp


#@rate_limit(limit=10)
@dp.message_handler(IsPrivateMessage())
async def command_error(message: types.Message):
    await message.answer(f'⚠️ The command "{message.text}" is not found.')
