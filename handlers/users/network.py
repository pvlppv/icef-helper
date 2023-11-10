from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='🗣 Network')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🗣 Network')
async def command_groups(message: types.Message):
    await message.answer(f'<b><ins>🗣 Channels:</ins></b>\n<a href="https://telegra.ph/file/81a44128672b043a0e44c.png">ㅤ</a>'
                         f'⭐️ <a href="https://t.me/icefofficial">ICEF Official</a>\n'
                         f'🧑🏼‍💼 <a href="https://t.me/asc_icef">ASC ICEF</a>\n'
                         f'💼 <a href="https://t.me/icefcareerservices">ICEF Career Services</a>\n'
                         f'💸 <a href="https://t.me/keystone_vacancies">Keystone</a>\n'
                         f'💡 <a href="https://t.me/cchse">HSE Case Club</a>\n'
                         f'🎉 <a href="https://t.me/icefcrew">ICEFcrew</a>\n\n'
                         f'<b><ins>🗣 Chats:</ins></b>\n' 
                         # f'🏦 <a href="https://t.me/+e3QpUVJPNGllY2Qy">Банковское дело и финансы</a>\n'
                         # f'💵 <a href="https://t.me/+AiPkmViMJIUyODNi">Экономика и менеджмент</a>\n'
                         # f'💴 <a href="https://t.me/+5Rr6bU-BeLkyYThi">Экономика</a>\n'
                         # f'💶 <a href="https://t.me/+sdKWhMDTqn83NzVi">Экономика и финансы</a>\n'
                         # f'🗄 <a href="https://t.me/+u40sufwsCr8xMWRi">Бухгалтерский учёт и финансы</a>\n'
                         # f'💷 <a href="https://t.me/+vxHbg9Rp70ZmZDgy">Экономика и математика</a>\n'
                         f'🐍 <a href="https://t.me/+Skq4_yKO5vk2ZDEy">IT</a>\n'
                         f'📈 <a href="https://t.me/+RBLPm1Gp27gyMzdi">Trading</a>\n'
                         f'🎵 <a href="https://t.me/+Paw8Zu4MVLMwYjIy">Music</a>\n'
                         f'🇫🇷 <a href="https://t.me/+7QL1Oi_nQ_Q5M2Uy">French</a>\n'
                         f'🇮🇹 <a href="https://t.me/+RqjHvVMG0_A4MGE6">Italian</a>\n'
                         f'🇩🇪 <a href="https://t.me/+USLA_VkUKMIyZjBi">Deutsch</a>\n'
                         f'🇪🇸 <a href="https://t.me/+aFwD5Npe7m5jYzYy">Spanish</a>\n'
                         f'🇨🇳 <a href="https://t.me/+D-ohKxr8WnplN2Iy">Chinese</a>\n'
                         f'🇦🇪 <a href="https://t.me/+V6exJ6UYkzM5YWYy">Arabic</a>\n'
                         f'🏋️ <a href="https://t.me/+Xfg7z3AgUU1jZDMy">Sport</a>\n\n'
                         f'<b><ins>🗣 Sticker Packs:</ins></b>\n'
                         f"🧸 <a href='https://t.me/addstickers/ICEF26'>ICEF'26</a>\n"
                         f"🪆 <a href='https://t.me/addstickers/ICEF1yearStickers'>ICEF 1 year</a>\n"
                         )