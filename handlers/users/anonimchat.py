from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, IsSubscriberChannelMessage
from keyboards.default.keyboard_ICEFHelper import kb_networking
from keyboards.default.keyboard_anonimchat import kb_anonimchat, kb_anonimchat2, kb_anonimchat1
from loader import dp, db_sql
from states import anonimchat
from utils.misc import rate_limit


@rate_limit(limit=3, key='💋 Anonchat')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='💋 Anonchat')
async def anonimchat_command(message: types.Message):
    await message.answer("<b>💋 You've entered the <tg-spoiler>anonymous</tg-spoiler> chat.</b>\n\n"
                         '🔎 Search - search for the person to start the chat with\n'
                         '🚫 Exit - exit the anonymous chat <a href="https://telegra.ph/file/36ae53665353359e4455c.png">ㅤ</a>', reply_markup=kb_anonimchat)
    await anonimchat.anonimchat.set()

@dp.message_handler(content_types=['text'], state=anonimchat.anonimchat)
async def anonimchat_start(message: types.Message, state: FSMContext):
    try:
        if message.text == '🔎 Search':
            chat_two = db_sql.get_chat()
            queue_info = db_sql.get_queue(message.from_user.id)
            if db_sql.create_chat(message.from_user.id, chat_two) is False:
                if queue_info is not True:
                    db_sql.add_queue(message.from_user.id)
                    await dp.bot.send_message(message.from_user.id, '<b>🔎 Searching for the person is on.</b>', reply_markup=kb_anonimchat2)
                else:
                    await dp.bot.send_message(message.from_user.id, "<b>⚠️ You can't create the chat with yourself.</b>")
            else:
                await dp.bot.send_message(message.from_user.id, '<b>🔎 Searching for the person is on.</b>')
                await dp.bot.send_message(message.from_user.id, '<b>🔎 Person has been found. Communicate!</b>\n'
                                                                '🕳 Leave - leave the chat\n', reply_markup=kb_anonimchat1)
                await dp.bot.send_message(chat_two, '<b>🔎 Person has been found. Communicate!</b>\n'
                                                    '🕳 Leave - leave the chat', reply_markup=kb_anonimchat1)
        elif message.text == '🕳 Leave':
            chat_info = db_sql.get_active_chat(message.from_user.id)
            if chat_info is not False:
                db_sql.delete_chat(chat_info[0])
                await dp.bot.send_message(chat_info[1], '<b>🕳️ Person has left the chat.</b>\n'
                                                        '🔎 Search - search for the another person\n'
                                                        '🚫 Exit - exit the anonymous chat', reply_markup=kb_anonimchat)
                await dp.bot.send_message(message.from_user.id, "<b>🕳️ You've left the chat.</b>\n"
                                                                '🔎 Search - search for the another person\n'
                                                                '🚫 Exit - exit the anonymous chat', reply_markup=kb_anonimchat)
            else:
                await dp.bot.send_message(message.from_user.id, "<b>⚠️ There is no any chat.</b>")
        elif message.text == '🚫 Exit':
            await state.finish()
            queue_info = db_sql.get_queue(message.from_user.id)
            if queue_info is False:
                await dp.bot.send_message(message.from_user.id, "<b>🔎 You're not in searching.</b>")
            else:
                db_sql.delete_queue(message.from_user.id)
            chat_info = db_sql.get_active_chat(message.from_user.id)
            if chat_info is not False:
                db_sql.delete_chat(chat_info[0])
                await dp.bot.send_message(chat_info[1], '<b>🕳️ Person has left the chat.</b>\n'
                                                        '🔎 Search - search for an another person\n'
                                                        '🚫 Exit - exit the anonymous chat', reply_markup=kb_anonimchat)
                await dp.bot.send_message(message.from_user.id, "<b>🕳️ You've left the chat.</b>", reply_markup=kb_anonimchat)
            else:
                await dp.bot.send_message(message.from_user.id, "<b>💋 You've exited the anonymous chat.</b>", reply_markup=kb_networking)

        else:
            chat_info = db_sql.get_active_chat(message.from_user.id)
            await dp.bot.send_message(chat_info[1], message.text)
    except TypeError:
        pass