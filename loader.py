from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

from utils.db_api.db_gino import db
from utils.dp_SQLStudio.db import Database

db_sql = Database('/Users/pavelpopov/PycharmProjects/ICEF Helper/dp_SQLStudio.db')
# db_sql = Database('/root/bot/dp_SQLStudio.db')


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


__all__ = ['bot','storage', 'dp', 'db', 'db_sql']