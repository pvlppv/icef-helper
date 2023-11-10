# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# def buy_menu(IsUrl=True, url='', bill=''):
#     QiwiMenu = InlineKeyboardMarkup(row_width=1)
#     if IsUrl:
#         btnUrlQIWI = InlineKeyboardButton(text='💳 Pay', url=url)
#         QiwiMenu.insert(btnUrlQIWI)
#
#     btnCheckQIWI = InlineKeyboardButton(text='Check payment status', callback_data='check_'+bill)
#     QiwiMenu.insert(btnCheckQIWI)
#     return QiwiMenu
