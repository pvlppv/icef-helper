from aiogram import types

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_locations import ikb_locations, ikb_locations2
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='🚪 Locations')
@dp.message_handler(text='🚪 Locations')
async def command_locations(message: types.Message):
    await message.answer(f'<b>🚪 Locations:</b> <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>', reply_markup=ikb_locations)

@dp.callback_query_handler(text='locations2')
async def command_locations2(call: types.CallbackQuery):
    await call.message.edit_text('<b>🚪 Locations:</b> <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>', reply_markup=ikb_locations)

@dp.callback_query_handler(text='important_locations')
async def command_importantlocations(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f"<b>📌 Important locations:</b>\n"
                                 f"T820 - room of curators (questions about student life)\n"
                                 f"T807 - room of inspector (questions about schedule, marks, transfer)\n"
                                 f"T818 - room of coordinator (questions about rating)\n"
                                 f"T820 - room of IT-specialist (questions about info-system, LMS)\n"
                                 f"T808 - financial department (questions about contract, payments)\n"
                                 f"T816 - ICEF career center (questions about internship, mentoring program, resume)\n"
                                 f"T108 - printing office\n"
                                 f"M106 - medical center\n"
                                 f"S012 - lost things", reply_markup=ikb_locations2)

@dp.callback_query_handler(text='libraries')
async def command_libraries(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f"<b>📚 Libraries:</b>\n"
                                 f"S104 - ICEF library\n"
                                 f"S106 - ICEF reading room", reply_markup=ikb_locations2)

@dp.callback_query_handler(text='co-working_rooms')
async def command_coworkingrooms(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f"<b>📝 Co-working rooms:</b>\n"
                                 f"S722 - ICEF co-working\n"
                                 f"S712 - co-working\n"
                                 f"T822 - co-working\n"
                                 f"N205 - co-working\n"
                                 f"N206 - co-working", reply_markup=ikb_locations2)

@dp.callback_query_handler(text='computer_classes')
async def command_computerclasses(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f"<b>💻 Computer classes:</b>\n"
                                 f"S712 - ICEF computer class", reply_markup=ikb_locations2)

@dp.callback_query_handler(text='chill_zones')
async def command_chilzones(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f"<b>🌬 Chill-zones:</b>\n"
                                 f"R309 - Chill-zone 1\n"
                                 f"R409 - Chill-zone 2\n"
                                 f"R507 - Chill-zone 3", reply_markup=ikb_locations2)

@dp.callback_query_handler(text='other_locations')
async def command_otherlocations(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>🚪 Locations:</b>\n\n <a href="https://telegra.ph/file/86b73b411c3f0a81598e5.png">ㅤ</a>'
                                 f'<b>⛳️ Other locations:</b>\n'
                                 f"T203 - gym\n"
                                 f"Z, floor 0 - table tennis\n"
                                 f"Canteen/Library, floor 2/R409 - charging stations\n"
                                 f"R508 - psychologist", reply_markup=ikb_locations2)