import asyncio
import json
from aiogram.utils.markdown import hlink

from aiogram import types
from aiogram.utils import json, executor
from gino import Gino

from filters import IsDatabaseUserMessage, IsPrivateMessage, IsSUPERGROUPMessage
from handlers.users.group_handlers.news_main_parsing import check_news_update
from loader import dp, bot
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit



# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), text='🗞 ICEF news')
# async def command_menu(message: types.Message):
#     await message.answer('<b>ICEF news from icef.hse.ru:</b>', reply_markup=kb_news)

# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), text='⬅️ Back')
# async def command_menu(message: types.Message):
#     await message.answer('Menu 2:', reply_markup=kb_menu2)

@rate_limit(limit=3, key='/news')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/news')
async def get_all_news(message: types.Message):
    await message.answer(f"<b>Last ICEF news from icef.hse.ru:</b>")
    check_news_update()
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/group_handlers/icef_news_icefhse.json") as file:
    with open("/root/bot/handlers/users/group_handlers/icef_news_icefhse.json") as file:
        news_dict = json.load(file)

    for k, v in news_dict.items():
        news = f"<b>{v['article_date_time']}</b>\n\n" \
               f"{hlink(v['article_title'], v['article_url'])}\n\n" \
               f"{v['article_desc']}"

        # более продвинутое форматирование
        # news = f"{hbold(v['article_date_time'])}\n\n" \
        #        f"{hunderline(v['article_title'])}\n\n" \
        #        f"{hcode(v['article_desc'])}\n\n" \
        #        f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)


# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), text='/last_news')
# async def get_last5_news(message: types.Message):
#     with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/parsing/icef_news_icefhse.json") as file:
#         news_dict = json.load(file)
#
#     for k, v in sorted(news_dict.items())[-5:]:
#         news = f"<b>{v['article_date_time']}</b>\n\n" \
#                f"{hlink(v['article_title'], v['article_url'])}\n\n" \
#                f"{v['article_desc']}"
#         await message.answer(news)

# @rate_limit(limit=3, key='Fresh news')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), text='Fresh news')
# async def get_fresh_news(message: types.Message):
#     await message.answer(f"<b>Fresh ICEF news from icef.hse.ru:</b>")
#     fresh_news = check_news_update()
#
#     if len(fresh_news) >= 1:
#         for k, v in sorted(fresh_news.items()):
#             news = f"<b>{v['article_date_time']}</b>\n\n" \
#                    f"{hlink(v['article_title'], v['article_url'])}\n\n" \
#                    f"{v['article_desc']}"
#
#             await message.answer(news)
#
#     else:
#         await message.answer("There is no fresh news.")



# рассылка новостей автоматическиasync
# async def news_every_minute():
#     while True:
#         fresh_news = check_news_update()
#
#         if len(fresh_news) >= 1:
#             for k, v in sorted(fresh_news.items()):
#                 news = f"<b>{v['article_date_time']}</b>\n\n" \
#                        f"{hlink(v['article_title'], v['article_url'])}\n\n" \
#                        f"{v['article_desc']}"
#
#                 users = await commands.select_all_users()
#                 for user in users:
#                     try:
#                         await bot.send_message(chat_id=user.user_id, text=news, disable_notification=True)
#                     except Exception:
#                         pass
#         # else:
#         #     await bot.send_message(admin, "NO NEWS.", disable_notification=True)
#
#         await asyncio.sleep(30)
#
# loop.create_task(news_every_minute())
#
#
