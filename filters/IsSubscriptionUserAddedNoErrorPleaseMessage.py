# from aiogram.dispatcher.filters import BoundFilter
# from aiogram.dispatcher.handler import CancelHandler
# from aiogram.types import Message, CallbackQuery
#
# from keyboards.inline import ikb_start
# from loader import db_sql
#
#
# class IsSubscriptionUserAddedNoErrorPleaseMessage(BoundFilter):
#     async def check(self, message: Message) -> bool:
#         if db_sql.user_exists(message.from_user.id):
#             return True
#         else:
#             db_sql.add_user(message.from_user.id)
#
#
# class IsSubscriptionUserAddedNoErrorPleaseCallback(BoundFilter):
#     async def check(self, call: CallbackQuery) -> bool:
#         if db_sql.user_exists(call.from_user.id):
#             return True
#         else:
#             db_sql.add_user(call.from_user.id)
