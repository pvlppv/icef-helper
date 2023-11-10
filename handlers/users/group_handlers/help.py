from aiogram import types
from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from loader import dp
from utils.misc import rate_limit

@rate_limit(limit=3, key='/help')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/help')
async def command_professors(message: types.Message):
    await message.answer(f"<b>Group commands</b>:\n\n"
                         f"👤 /profile - личный профиль\n"
                         f"👤 /checkprofile - чужой профиль\n"
                         # f"🗃 /handbook - справочник студента\n"
                         f"📂 /materials - полезные материалы по учёбе и работе\n"
                         f"🗣 /chats - чаты по интересам\n"
                         # f"🗞 /news - новости с icef.hse.ru\n"
                         # f"🎫 /events - ближайшие события с icef.hse.ru\n"
                         f"🔔 /timetable - расписание пар у всех групп\n"
                         f"👨🏼‍🏫 /professors - контакты профессоров")
