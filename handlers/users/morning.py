import asyncio
import calendar
import datetime
from datetime import date

import aioschedule
import requests
import ruz
from aiogram import types
import json

from aiogram.utils.exceptions import MessageTextIsEmpty

from keyboards.inline.inline_keyboard_morning import ikb_morning
from aiogram.utils.markdown import hlink

from loader import dp
from utils.db_api import quick_commands

async def morning():
    response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
    json_data = response.json()
    data = json_data['data']
    # users = await quick_commands.select_all_users()
    datetimeobject = datetime.datetime.now()
    await dp.bot.send_message(chat_id=384993580, text=f'☀️ {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}.\n\n'
                              f'Good morning.\n\n'
                              f'«{data[0]["quoteText"]}»', reply_markup=ikb_morning)

@dp.callback_query_handler(text='morning_lessons')
async def morning_lessons(call: types.CallbackQuery):
    try:
        await call.message.answer('<b>🗓️ Schedule for today:</b>')
        user = await quick_commands.select_user(call.from_user.id)
        schedule0 = ruz.person_lessons(email=user.email, from_date=f'{date.today()}', to_date=f'{date.today()}')
        _schedule0 = ''
        for elements in schedule0:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule0 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        await call.message.answer('<b>No lessons for today.</b>')

@dp.callback_query_handler(text='morning_news')
async def morning_news(call: types.CallbackQuery):
    await call.message.answer('<b>🗞 Fresh news from icef.hse.ru and icefstudents.hse.ru:</b>')
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefhse.json") as file:
    with open("/root/bot/icef_news_icefhse.json") as file:
        icef_news_icefhse = json.load(file)
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefstudents.json") as file:
    with open("/root/bot/icef_news_icefstudents.json") as file:
        icef_news_icefstudents = json.load(file)
    for k, v in list(reversed(icef_news_icefhse.items()))[:1]:
        news = f"<b>{v['article_date_time']}</b>\n\n" \
               f"{hlink(v['article_title'], v['article_url'])}\n\n" \
               f"{v['article_desc']}"
        await call.message.answer(news)
    for k, v in list(reversed(icef_news_icefstudents.items()))[:1]:
        news = f"<b>{v['date']}</b>\n\n" \
               f"{hlink(v['title'], v['url'])}\n\n" \
               f"{v['desc']}"
        await call.message.answer(news)

@dp.callback_query_handler(text='morning_events')
async def morning_events(call: types.CallbackQuery):
    await call.message.answer('<b>🎫 Upcoming events:</b>')
    # f = open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_events.txt", "r")
    f = open("/root/bot/icef_events.txt", "r")
    icef_events = f.read()
    f.close()
    await call.message.answer(f'{icef_events}')



async def scheduler_morning():
    aioschedule.every().day.at('08:00').do(morning)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
