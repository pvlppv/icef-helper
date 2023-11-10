import json

from aiogram import types
from aiogram.utils import json
from aiogram.utils.markdown import hlink

from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_news import ikb_news
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='🗞 News')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🗞 News')
async def get_all_news(message: types.Message):
    await message.answer('<b>🗞 ICEF News:</b><a href="https://telegra.ph/file/86cf78ea9e11fc19fddd3.png">ㅤ</a>', reply_markup=ikb_news)

@dp.callback_query_handler(text='news_icefhse')
async def get_news_icefhse(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>🗞 Last news from icef.hse.ru:</b>")
    with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefhse.json") as file:
    # with open("/root/bot/icef_news_icefhse.json") as file:
        icef_news_icefhse = json.load(file)

    for k, v in icef_news_icefhse.items():
        news = f"<b>{v['article_date_time']}</b>\n\n" \
               f"{hlink(v['article_title'], v['article_url'])}\n\n" \
               f"{v['article_desc']}"
        await call.message.answer(news)

@dp.callback_query_handler(text='news_icefstudents')
async def get_news_icefstudents(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>🗞 Last news from icefstudents.hse.ru:</b>")
    with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefstudents.json") as file:
    # with open("/root/bot/icef_news_icefstudents.json") as file:
        icef_news_icefstudents = json.load(file)

    for k, v in icef_news_icefstudents.items():
        news = f"<b>{v['date']}</b>\n\n" \
               f"{hlink(v['title'], v['url'])}\n\n" \
               f"{v['desc']}"
        await call.message.answer(news)