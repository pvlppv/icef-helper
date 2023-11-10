import asyncio
import json
from aiogram.utils.markdown import hlink

from aiogram import types
from aiogram.utils import json

from filters import IsDatabaseUserMessage, IsPrivateMessage, IsSUPERGROUPMessage
from handlers.users.group_handlers.events_main_parsing import check_events_update
from loader import dp, bot
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit


# @rate_limit(limit=3, key='🎫 ICEF events')
# @dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), text='🎫 ICEF events')
# async def command_menu(message: types.Message):
#     await message.answer(f"<b>Closest ICEF events:</b>")

@rate_limit(limit=3, key='/events')
@dp.message_handler(IsSUPERGROUPMessage(), IsDatabaseUserMessage(), text='/events')
async def get_all_events(message: types.Message):
    await message.answer(f"<b>ICEF events from icef.hse.ru:</b>")
    check_events_update()
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/group_handlers/0events_dict.json") as file:
    with open("/root/bot/handlers/users/group_handlers/0events_dict.json") as file:
        events_dict = json.load(file)

    for k, v in events_dict.items():
        events = f"📍 " \
                 f"{hlink(v['article_title'], v['article_url'])}\n\n" \
                 f"<b>Date: </b>" \
                 f"{v['article_date']}\n" \
                 f"<b>Time: </b>" \
                 f"{v['article_time']}\n" \
                 f"<b>Address: </b>" \
                 f"{v['article_address']}"

        await message.answer(events)


# async def events_every_minute():
#     while True:
#         new_events = check_events_update()
#
#         if len(new_events) >= 1:
#             for k, v in sorted(new_events.items()):
#                 events = f"📍 " \
#                          f"{hlink(v['article_title'], v['article_url'])}\n\n" \
#                          f"<b>Date: </b>" \
#                          f"{v['article_date']}\n" \
#                          f"<b>Time: </b>" \
#                          f"{v['article_time']}\n" \
#                          f"<b>Address: </b>" \
#                          f"{v['article_address']}"
#
#                 users = await commands.select_all_users()
#                 for user in users:
#                     try:
#                         await bot.send_message(chat_id=user.user_id, text=events, disable_notification=True)
#                     except Exception:
#                         pass
#
#         # else:
#         #     await bot.send_message(admin, "NO EVENTS.", disable_notification=True)
#
#         await asyncio.sleep(30)
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.create_task(events_every_minute())
#
