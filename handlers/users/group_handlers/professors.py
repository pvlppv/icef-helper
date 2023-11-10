
from aiogram import types
from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from loader import dp
from utils.misc import rate_limit

@rate_limit(limit=3, key='/professors')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/professors')
async def command_professors(message: types.Message):
    await message.answer(f"<b>⚠️ [Soon]</b>\n\n<ins>Soon</ins> here will be a professors list with their contacts.")
