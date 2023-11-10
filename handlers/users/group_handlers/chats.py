from aiogram import types
from filters import IsDatabaseUserMessage, IsSUPERGROUPMessage
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='/chats')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/chats')
async def command_groups(message: types.Message):
    await message.answer(f'<b>🗣 Chats:</b>\n\n' 
                         f'<b>Specializations:</b>\n'
                         f'🏦 <a href="https://t.me/+e3QpUVJPNGllY2Qy">Банковское дело и финансы</a>\n'
                         f'💵 <a href="https://t.me/+AiPkmViMJIUyODNi">Экономика и менеджмент</a>\n'
                         f'💴 <a href="https://t.me/+5Rr6bU-BeLkyYThi">Экономика</a>\n'
                         f'💶 <a href="https://t.me/+sdKWhMDTqn83NzVi">Экономика и финансы</a>\n'
                         f'🗄 <a href="https://t.me/+u40sufwsCr8xMWRi">Бухгалтерский учёт и финансы</a>\n'
                         f'💷 <a href="https://t.me/+vxHbg9Rp70ZmZDgy">Экономика и математика</a>\n\n'
                         f'<b>Additional cources:</b>\n'
                         f'🐍 <a href="https://t.me/+Skq4_yKO5vk2ZDEy">Python</a>\n'
                         f'💿 <a href="https://t.me/+Zg2_ghQYKPk3MTBi">C#</a>\n'
                         f'📊 <a href="https://t.me/+X7z6GQnrqf84NGYy">Excel</a>\n'
                         f'📈 <a href="https://t.me/+RBLPm1Gp27gyMzdi">Trading</a>\n'
                         f'🎵 <a href="https://t.me/+Paw8Zu4MVLMwYjIy">Music</a>\n'
                         f'🇫🇷 <a href="https://t.me/+7QL1Oi_nQ_Q5M2Uy">French</a>\n'
                         f'🇮🇹 <a href="https://t.me/+RqjHvVMG0_A4MGE6">Italian</a>\n'
                         f'🇩🇪 <a href="https://t.me/+USLA_VkUKMIyZjBi">Deutsch</a>\n'
                         f'🇪🇸 <a href="https://t.me/+aFwD5Npe7m5jYzYy">Spanish</a>\n'
                         f'🇨🇳 <a href="https://t.me/+D-ohKxr8WnplN2Iy">Chinese</a>\n'
                         f'🇦🇪 <a href="https://t.me/+V6exJ6UYkzM5YWYy">Arabic</a>\n'
                         f'🏋️ <a href="https://t.me/+Xfg7z3AgUU1jZDMy">Gym</a>\n'
                         f'🧘 <a href="https://t.me/+xaBYPGMG79BiZjEy">Yoga</a>'
                         )