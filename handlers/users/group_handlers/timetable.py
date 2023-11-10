from aiogram import types

from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from loader import dp
from utils.misc import rate_limit

@rate_limit(limit=3, key='/timetable')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/timetable')
async def command_professors(message: types.Message):
    f = open("icef_events.txt", "r")
    timetable = f.read()
    f.close()
    await message.answer(timetable)



