import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from loader import dp, db_sql
from states.notifications import notifications
from utils.misc import rate_limit


@rate_limit(limit=3, key='notification')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='notification')
async def command_notifications(message: types.Message):
    await message.answer('Enter text:')
    await notifications.text.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=notifications.text)
async def notification_text(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer('Notification added.')
    await state.update_data(text=answer)
    await message.answer('Enter date:')
    await notifications.date.set()

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), state=notifications.date)
async def notification_date(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer('Date added.')
    data = await state.get_data()
    text = data.get('text')
    db_sql.add_notification(message.from_user.id, datetime.datetime.now(), answer, text)
    await state.finish()








