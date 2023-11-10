from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='🎫 Events')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🎫 Events')
async def command_icefevents(message: types.Message):
    f = open("/root/bot/icef_events.txt", "r")
    icef_events = f.read()
    f.close()
    await message.answer(f'<b>🎫 ICEF events:</b>\n\n <a href="https://telegra.ph/file/a5a0f32790645d24af63d.png">ㅤ</a>'
                         f'{icef_events}')



