from aiogram import types
from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage
from filters.IsSubscriberChannel import IsSubscriberChannelMessage
from keyboards.default.keyboard_ICEFHelper import kb_ICEFHelperMenu, kb_networking, kb_studying, kb_noticef
from keyboards.inline.inline_keyboard_homepage import ikb_homepage_back, ikb_homepage
from loader import dp
from utils.misc import rate_limit


@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Back')
async def keyboard_home_back(message: types.Message):
    await message.answer(f'<b>Home Page:</b>', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Home')
async def keyboard_home(message: types.Message):
    await message.answer(f'<b>Home Page:</b>', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Home ➡️')
async def keyboard_home_two(message: types.Message):
    await message.answer(f'<b>Home Page:</b>', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬇️ Home')
async def keyboard_home_three(message: types.Message):
    await message.answer(f'<b>Home Page:</b>', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='NOT ICEF')
async def keyboard_noticef(message: types.Message):
    await message.answer(f'<b>Not ICEF:</b>', reply_markup=kb_noticef)

        # f'<a href="https://telegra.ph/file/583950b796a300bc7d844.png">ㅤ</a>', reply_markup=kb_ICEFHelperMenu)
    # await message.answer('<u><b>🌐 ICEF Helper Home Page 🌐</b></u>\n\n\n<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
    #                      '<b>👤 Networking</b> - netw-ing section\n\n'
    #                      '<b>📚 Studying</b> - studying section\n\n'
    #                      '<b>⚙️ Settings</b> - bot-settings section\n\n\n'
    #                      '<b>🖥️ <a href="https://t.me/+DFuYOJt5rcpjMWZi">Telegram Channel</a></b>', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Helper')
async def keyboard_icefhelper_back(message: types.Message):
    await message.answer(f'<b>Home Page:</b>', reply_markup=kb_ICEFHelperMenu)
    # await message.answer('<u><b>🌐 ICEF Helper Home Page 🌐</b></u>\n\n\n<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
    #                      '<b>👤 Networking</b> - netw-ing section\n\n'
    #                      '<b>📚 Studying</b> - studying section\n\n'
    #                      '<b>⚙️ Settings</b> - bot-settings section\n\n\n'
    #                      '<b>🖥️ <a href="https://t.me/+DFuYOJt5rcpjMWZi">Telegram Channel</a></b>', reply_markup=kb_ICEFHelperMenu)

@rate_limit(limit=3, key='🌐 ICEF Helper')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🌐 ICEF Helper')
async def keyboard_icefhelper(message: types.Message):
    await message.answer(f'<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>', reply_markup=ikb_homepage)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Networking')
async def keyboard_networking_and_back(message: types.Message):
    await message.answer('<b>👤 Networking:</b>', reply_markup=kb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='👤 Networking')
async def keyboard_networking_two(message: types.Message):
    await message.answer('<b>👤 Networking:</b>', reply_markup=kb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Networking')
async def keyboard_icefnetworking_back(message: types.Message):
    await message.answer('<b>👤 Networking:</b>', reply_markup=kb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='Studying ➡️')
async def keyboard_studying(message: types.Message):
    await message.answer('<b>📚 Studying:</b>', reply_markup=kb_studying)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📚 Studying')
async def keyboard_studying_two(message: types.Message):
    await message.answer('<b>📚 Studying:</b>', reply_markup=kb_studying)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Studying')
async def keyboard_icefstudying_back(message: types.Message):
    await message.answer('<b>📚 Studying:</b>', reply_markup=kb_studying)

# command artem_chemerisov
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='💹')
async def keyboard_artem_chemerisov(message: types.Message):
    await message.answer('<b><a href="https://youtu.be/G1IbRujko-A">‍️Weekly GAGs by @archibaldIII.</a></b>')