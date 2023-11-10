import datetime
from datetime import date, timedelta, datetime
import calendar

from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty

from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage
from filters.IsSubscriberChannel import IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_schedule import ikb_schedule, ikb_schedule_general
from keyboards.inline.inline_keyboard_schedule_subjects import ikb_schedule_subjects
from loader import dp
import ruz.utils

from utils.misc import rate_limit
from utils.db_api import quick_commands

@rate_limit(limit=3, key='🗓️ Schedule')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='🗓️ Schedule')
async def command_ruz(message: types.Message):
    await message.answer("<b>🗓️ Schedule:</b>", reply_markup=ikb_schedule_general)

@dp.callback_query_handler(text='my_schedule')
async def command_my_schedule(call: types.CallbackQuery):
    await call.message.edit_text('<b>🗓️ My schedule:</b>', reply_markup=ikb_schedule)

@dp.callback_query_handler(text='schedule_back')
async def command_schedule_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>🗓️ Schedule:</b>', reply_markup=ikb_schedule_general)

@dp.callback_query_handler(text='schedule_today')
async def command_ruz_today(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        user = await quick_commands.select_user(call.from_user.id)
        schedule0 = ruz.person_lessons(email=user.email, from_date=f'{date.today()}', to_date=f'{date.today()}')
        _schedule0 = ''
        for elements_date in schedule0:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule0 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule0:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule0 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.edit_text('<b>🗓️ Schedule for today:</b>')
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        await call.message.answer('<b>No lessons for today.</b>')

@dp.callback_query_handler(text='schedule_tomorrow')
async def command_ruz_tomorrow(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        user = await quick_commands.select_user(call.from_user.id)
        schedule0 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
        _schedule0 = ''
        for elements_date in schedule0:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule0 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule0:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule0 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.edit_text('<b>🗓️ Schedule for tomorrow:</b>')
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        await call.message.answer('<b>No lessons for tomorrow.</b>')

@dp.callback_query_handler(text='schedule_week')
async def command_ruz_week(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        user = await quick_commands.select_user(call.from_user.id)
        schedule0 = ruz.person_lessons(email=user.email, from_date=f'{date.today()}', to_date=f'{date.today()}')
        _schedule0 = ''
        for elements_date in schedule0:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule0 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule0:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule0 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.edit_text('<b>🗓️ Schedule for week:</b>')
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
        _schedule1 = ''
        for elements_date in schedule1:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule1 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule1:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule1 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule1}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule2 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
        _schedule2 = ''
        for elements_date in schedule2:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule2 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule2:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule2 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule2}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule3 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
        _schedule3 = ''
        for elements_date in schedule3:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule3 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule3:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule3 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule3}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule4 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
        _schedule4 = ''
        for elements_date in schedule4:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule4 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule4:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule4 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule4}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule5 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
        _schedule5 = ''
        for elements_date in schedule5:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule5 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule5:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule5 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule5}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule6 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
        _schedule6 = ''
        for elements_date in schedule6:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule6 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule6:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule6 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule6}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule7 = ruz.person_lessons(email=user.email, from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
        _schedule7 = ''
        for elements_date in schedule7:
            date1 = elements_date.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            _schedule7 += f'<b><ins>📍 {datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}</ins></b>\n\n'
            break
        for elements in schedule7:
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            _schedule7 += f'🕓 <b>{begin_lesson} - {end_lesson}</b>\n' \
                          f'<b>{title}</b>\n' \
                          f'{professor}\n' \
                          f'<b>{auditorium}</b>\n\n'
        await call.message.answer(f'{_schedule7}')
    except MessageTextIsEmpty:
        pass