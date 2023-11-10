from aiogram import types
from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage
from filters.IsSubscriberChannel import IsSubscriberChannelMessage
from keyboards.default.keyboard_ICEFHelper import kb_ICEFHelperMenu, kb_networking, kb_studying
from keyboards.inline.inline_keyboard_homepage import ikb_homepage
from keyboards.inline.inline_keyboard_icefnetworking import ikb_networking
from keyboards.inline.inline_keyboard_icefstudying import ikb_studying
from loader import dp
from utils.db_api import quick_commands


@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🌐 Home Page')
async def keyboard_homepage(message: types.Message):
    await message.answer(f'<a href="https://telegra.ph/file/281d592daec2a4af63027.png">ㅤ</a>', reply_markup=ikb_homepage)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Helper')
async def keyboard_icefhelper(message: types.Message):
    await message.answer('<u><b>🌐 ICEF Helper Home Page 🌐</b></u>\n\n\n<a href="https://telegra.ph/file/8fee30b60e64e731f7162.png">ㅤ</a>'
                         '<b>👤 Networking</b> - netw-ing section\n\n'
                         '<b>📚 Studying</b> - studying section\n\n'
                         '<b>⚙️ Settings</b> - bot-settings section\n\n\n', reply_markup=kb_ICEFHelperMenu)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='👤 Networking')
async def keyboard_networking(message: types.Message):
    await message.answer('<a href="https://telegra.ph/file/3411add02351ba4460088.png">ㅤ</a>', reply_markup=ikb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='👤 ICEF Networking')
async def keyboard_icefnetworking(message: types.Message):
    await message.answer('<b>👤 ICEF Networking:</b>', reply_markup=ikb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Networking')
async def keyboard_icefnetworking_back(message: types.Message):
    await message.answer('<b>👤 ICEF Networking:</b>', reply_markup=kb_networking)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📚 Studying')
async def keyboard_studying(message: types.Message):
    await message.answer('<a href="https://telegra.ph/file/8bd552ee5b6a661a69a69.png">ㅤ</a>', reply_markup=ikb_studying)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='📚 ICEF Studying')
async def keyboard_icefstudying(message: types.Message):
    await message.answer('<b>📚 ICEF Studying:</b>', reply_markup=kb_studying)

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ ICEF Studying')
async def keyboard_icefstudying_back(message: types.Message):
    await message.answer('<b>📚 ICEF Studying:</b>', reply_markup=kb_studying)

# command artem chemerisov
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='💹')
async def keyboard_artem_chemerisov(message: types.Message):
    await message.answer('<b><a href="https://youtu.be/G1IbRujko-A">‍️Weekly GAGs by @archibaldIII.</a></b>')

@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='⬅️ Subjects')
async def keyboard_oldsubjects_back(message: types.Message):
    await message.answer('<b>📚 ICEF Studying:</b>', reply_markup=kb_studying)
