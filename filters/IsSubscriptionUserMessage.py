# from aiogram.dispatcher.filters import BoundFilter
# from aiogram.dispatcher.handler import CancelHandler
# from aiogram.types import Message, CallbackQuery
# from handlers.users.subscription import time_sub_day
#
# from keyboards.inline import ikb_start
# from loader import db_sql
#
#
# class IsSubscriptionUserMessage(BoundFilter):
#     async def check(self, message: Message) -> bool:
#         if db_sql.user_exists(message.from_user.id):
#             sub = time_sub_day(db_sql.get_sub_time(message.from_user.id))
#             sub_time_zero = '0'
#             if sub == False:
#                 db_sql.set_sub_time(message.from_user.id, sub_time_zero)
#             user = db_sql.get_sub_time(message.from_user.id)
#             if user:
#                 return True
#             else:
#                 await message.answer(f'⭐️ Full access to the bot is only for the subscribers.\n\n'
#                                      f'Click the button below to get more information.', reply_markup=ikb_start)
#                 raise CancelHandler()
#         else:
#             db_sql.add_user(message.from_user.id)
#             sub = time_sub_day(db_sql.get_sub_time(message.from_user.id))
#             sub_time_zero = '0'
#             if sub == False:
#                 db_sql.set_sub_time(message.from_user.id, sub_time_zero)
#             user = db_sql.get_sub_time(message.from_user.id)
#             if user:
#                 return True
#             else:
#                 await message.answer(f'⭐️ Full access to the bot is only with the subscription.\n\n'
#                                      f'Click the button below to get more information.', reply_markup=ikb_start)
#                 raise CancelHandler()
#
#
#
# class IsSubscriptionUserCallback(BoundFilter):
#     async def check(self, call: CallbackQuery) -> bool:
#         if db_sql.user_exists(call.from_user.id):
#             sub = time_sub_day(db_sql.get_sub_time(call.from_user.id))
#             sub_time_zero = '0'
#             if sub == False:
#                 db_sql.set_sub_time(call.from_user.id, sub_time_zero)
#             user = db_sql.get_sub_time(call.from_user.id)
#             if user:
#                 return True
#             else:
#                 await call.message.answer(f'⭐️ Full access to the bot is only with the subscription.\n\n'
#                                      f'Click the button below to get more information.', reply_markup=ikb_start)
#                 raise CancelHandler()
#         else:
#             db_sql.add_user(call.from_user.id)
#             sub = time_sub_day(db_sql.get_sub_time(call.from_user.id))
#             sub_time_zero = '0'
#             if sub == False:
#                 db_sql.set_sub_time(call.from_user.id, sub_time_zero)
#             user = db_sql.get_sub_time(call.from_user.id)
#             if user:
#                 return True
#             else:
#                 await call.message.answer(f'⭐️ Full access to the bot is only with the subscription.\n\n'
#                                      f'Click the button below to get more information.', reply_markup=ikb_start)
#                 raise CancelHandler()
