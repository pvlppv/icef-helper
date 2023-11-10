from aiogram import types
from aiogram.dispatcher import FSMContext
from youtubesearchpython import VideosSearch
from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_study_search import ikb_study_search
from loader import dp
from states.youtube_search import youtube_search
from utils.misc import rate_limit
import hashlib
import json
import requests
from bs4 import BeautifulSoup

@rate_limit(limit=3, key='📟 Study Search')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📟 Study Search')
async def command_study_search(message: types.Message):
    await message.answer('Enter search:')
    await youtube_search.search.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=youtube_search.search)
async def study_search_state(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(search=answer)
    await message.answer(f'<b>📟 Study Search:</b>\n\n'
                         f'Where to search "<i>{answer}</i>"?', reply_markup=ikb_study_search)

@dp.callback_query_handler(text='study_search_youtube', state=youtube_search.search)
async def command_youtube_search(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    search = data.get('search')
    print(search)
    videosSearch = VideosSearch(query=search, limit=10)
    for i in range(10):
        title = videosSearch.result()['result'][i]['title']
        published_time = videosSearch.result()['result'][i]['publishedTime']
        duration = videosSearch.result()['result'][i]['duration']
        view_count = videosSearch.result()['result'][i]['viewCount']['short']
        link = videosSearch.result()['result'][i]['link']
        await call.message.answer(f'<b>Title:</b> <a href="{link}">{title}</a>\n'
                                  f'<b>Duration:</b> {duration}\n'
                                  f'<b>Published time:</b> {published_time}\n'
                                  f'<b>View count:</b> {view_count}')
    await state.finish()

# inline mode
# @dp.inline_handler()
# async def youtube_search_show(query: types.InlineQuery):
#     text = query.query or 'echo'
#     links = await youtube_search(text)
#     articles = [types.InlineQueryResultArticle(
#         id = hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
#         title = f'{link["title"]}',
#         url = f'https://www.youtube.com/watch?v={link["id"]}',
#         thumb_url = f'{link["thumbnails"][0]}',
#         input_message_content = types.InputMessageContent(message_text=f'https://www.youtube.com/watch?v={link["id"]}')
#     ) for link in links]
#
#     await query.answer(articles, cache_time=60, is_personal=True)

