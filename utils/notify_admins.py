import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = '<b>ICEF Helper is on.</b>'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)

async def on_shotdown_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = '<b>ICEF Helper is off.</b>'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
