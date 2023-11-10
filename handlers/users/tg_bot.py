#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import telebot
# from telebot import types
from aiogram import types
from aiogram.types import ContentType

from handlers.users import analytics
from handlers.users.analytics import statistics, analysis, remove
from loader import dp

# token = ""
# bot = telebot.TeleBot(token)

# user_markup = types.ReplyKeyboardMarkup(True)
# user_markup.row('команда а', 'команда б')
# user_markup.row('команда в')
#
#
# @dp.message_handler(commands=['start'])
# def handle_text(message):
#     analytics.statistics(message.chat.id, message.text)
#     bot.send_message(message.chat.id, " Исполнена команда старт ", reply_markup=user_markup)

@dp.message_handler(text='command')
async def handle_text(message: types.Message):
    statistics(message.from_user.id, message.text)
    await message.answer('Использована команда')

@dp.message_handler(text='command a')
async def command_a(message: types.Message):
    statistics(message.from_user.id, message.text)
    await message.answer('command a used')

@dp.message_handler(text='command b')
async def command_b(message: types.Message):
    statistics(message.from_user.id, message.text)
    await message.answer('command b used')

@dp.message_handler(text='command c')
async def command_c(message: types.Message):
    statistics(message.from_user.id, message.text)
    await message.answer('command c used')

# @dp.message_handler(content_types=ContentType)
# async def command_d(message: types.Message):
#     statistics(message.from_user.id, message.text)

# @dp.message_handler(content_types='text')
# async def command_statistics(message: types.Message):
#     if message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
#         st = message.text.split(' ')
#         if 'txt' in st or 'тхт' in st:
#             analysis(st, message.from_user.id)
#             with open('%s.txt' %message.from_user.id ,'r',encoding='UTF-8') as file:
#                 await message.answer_document(file)
#             remove(message.from_user.id)
#         else:
#             messages = analysis(st, message.from_user.id)
#             await message.answer(messages)
