import calendar
from datetime import datetime, date, timedelta

import ruz.utils
from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty

from filters import IsPrivateMessage, IsSubscriptionUserMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage
from keyboards.inline.inline_keyboard_professors import ikb_SmartLMS_professors, ikb_SmartLMS_professors_back, \
    ikb_statistics_professors, ikb_ics_professors, ikb_philosophy_professors, ikb_history_professors, \
    ikb_microeconomics_professors
from keyboards.inline.inline_keyboard_professors import ikb_calculus_professors, ikb_professors_info, ikb_professors_schedule
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='👨🏻‍🏫 Professors')
@dp.message_handler(IsPrivateMessage(), IsDatabaseUserMessage(), IsAcceptedUserMessage(), IsSubscriberChannelMessage(), text='👨🏻‍🏫 Professors')
async def command_professors(message: types.Message):
    await message.answer('<b>👨🏻‍🏫 Professors:</b>', reply_markup=ikb_professors_info)

@dp.callback_query_handler(text='professors_back')
async def command_professors_schedule_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>👨🏻‍🏫 Professors Schedule:</b>', reply_markup=ikb_professors_schedule)

@dp.callback_query_handler(text='professors_info')
async def command_professors_info(call: types.CallbackQuery):
    await call.message.edit_text('<b>👨🏻‍🏫 Professors Info:</b>', reply_markup=ikb_professors_info)

@dp.callback_query_handler(text='professors_schedule')
async def command_professors_schedule(call: types.CallbackQuery):
    await call.message.edit_text('<b>👨🏻‍🏫 Professors Schedule:</b>', reply_markup=ikb_professors_schedule)

@dp.callback_query_handler(text='calculus_professors')
async def command_calculus_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus professors schedule:</b>', reply_markup=ikb_calculus_professors)

@dp.callback_query_handler(text='statistics_professors')
async def command_statistics_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics professors schedule:</b>', reply_markup=ikb_statistics_professors)

@dp.callback_query_handler(text='microeconomics_professors')
async def command_microeconomics_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics professors schedule:</b>', reply_markup=ikb_microeconomics_professors)

@dp.callback_query_handler(text='history_professors')
async def command_history_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History professors schedule:</b>', reply_markup=ikb_history_professors)

@dp.callback_query_handler(text='philosophy_professors')
async def command_philosophy_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📒 Philosophy professors schedule:</b>', reply_markup=ikb_philosophy_professors)

@dp.callback_query_handler(text='ics_professors')
async def command_ics_professors(call: types.CallbackQuery):
    await call.message.edit_text('<b>📓 ICS professors schedule:</b>', reply_markup=ikb_ics_professors)

@dp.callback_query_handler(text='calculus_professors_patrik')
async def calculus_professors_patrik(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Patrick's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='apatrik@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_zhukov')
async def calculus_professors_zhukov(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Zhukov's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='pzhukov@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_vorchik')
async def calculus_professors_vorchik(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Vorchik's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='avorchik@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_luk')
async def calculus_professors_luk(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Lukyanchenko's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='plukyanchenko@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_brikov')
async def calculus_professors_brikov(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Brykov's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='vbrykov@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_shelike')
async def calculus_professors_shelike(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Shelike's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ashelike@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='calculus_professors_hassan')
async def calculus_professors_hassan(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Khassan's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ykhassan@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='statistics_professors_lyulko')
async def statistics_professors_lyulko(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Lyulko's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ylyulko@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='statistics_professors_zhitlukhin')
async def statistics_professors_zhitlukhin(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Zhitlukhin's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='mzhitlukhin@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='statistics_professors_potapov')
async def statistics_professors_potapov(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Potapov's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='dipotapov@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_yurko')
async def microeconomics_professors_yurko(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Yurko's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ayurko@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_avtonomov')
async def microeconomics_professors_avtonomov(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Avtonomov's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='yavtonomov@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_verem')
async def microeconomics_professors_verem(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Verem's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='iverem@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_vekilyan')
async def microeconomics_professors_vekilyan(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Vekilyan's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='avekilyan@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_chernyshova')
async def microeconomics_professors_chernyshova(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Chernyshova's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ychernyshova@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='microeconomics_professors_zimrutyan')
async def microeconomics_professors_zimrutyan(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Zimrutyan's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='gzimrutyan@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='history_professors_tsareva')
async def history_professors_tsareva(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Tsareva's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='atsareva@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='history_professors_otdelnov')
async def history_professors_otdelnov(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Otdelnov's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='motdelnov@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='history_professors_petrova')
async def history_professors_petrova(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Petrova's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='mspetrova@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='philosophy_professors_seir')
async def philosophy_professors_seir(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Sairsingh's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='sairsingh@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='ics_professors_akinshin')
async def ics_professors_akinshin(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Akinshin's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='aakinshin@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='ics_professors_bessonova')
async def ics_professors_bessonova(call: types.CallbackQuery):
    try:
        await call.message.edit_text('Logging in to HSE RUZ...')
        schedule0 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today()}', to_date=f'{date.today()}')
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
        await call.message.edit_text("<b>🗓️ Bessonova's schedule for week:</b>")
        await call.message.answer(f'{_schedule0}')
    except MessageTextIsEmpty:
        pass
    try:
        schedule1 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=1)}', to_date=f'{date.today() + timedelta(days=1)}')
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
        schedule2 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=2)}', to_date=f'{date.today() + timedelta(days=2)}')
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
        schedule3 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=3)}', to_date=f'{date.today() + timedelta(days=3)}')
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
        schedule4 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=4)}', to_date=f'{date.today() + timedelta(days=4)}')
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
        schedule5 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=5)}', to_date=f'{date.today() + timedelta(days=5)}')
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
        schedule6 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=6)}', to_date=f'{date.today() + timedelta(days=6)}')
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
        schedule7 = ruz.person_lessons(email='ibes@hse.ru', from_date=f'{date.today() + timedelta(days=7)}', to_date=f'{date.today() + timedelta(days=7)}')
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

@dp.callback_query_handler(text='SmartLMS_professors_back')
async def command_professors_info_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>👨🏻‍🏫 Professors Info:</b>', reply_markup=ikb_professors_info)

@dp.callback_query_handler(text='SmartLMS_calculus_professors')
async def command_calculus_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📘 Calculus professors:</b>\n\n"
                         f"👤 <b>Патрик Анатолий Евгеньевич</b>\n"
                         f"- apatrik@hse.ru\n\n"
                         f"👤 <b>Жуков Павел Владимирович</b>\n"
                         f"- pzhukov@hse.ru\n\n"
                         f"👤 <b>Ворчик Андрей Денисович</b>\n"
                         f"- avorchik@hse.ru\n\n"
                         f"👤 <b>Лукьянченко Пётр Павлович</b>\n"
                         f"- plukyanchenko@hse.ru\n\n"
                         f"👤 <b>Брыков Вячеслав Вячеславович</b>\n"
                         f"- vbrykov@hse.ru\n\n"
                         f"👤 <b>Шелике Аяна Георгиевна</b>\n"
                         f"- ashelike@hse.ru\n\n"
                         f"👤 <b>Хассан Яна Нибаль</b>\n"
                         f"- ykhassan@hse.ru"
                         , reply_markup=ikb_SmartLMS_professors_back)

@dp.callback_query_handler(text='SmartLMS_statistics_professors')
async def command_statistics_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📗 Statistics professors:</b>\n\n"
                         f"👤 <b>Патрик Анатолий Евгеньевич</b>\n"
                         f"- apatrik@hse.ru\n\n"
                         f"👤 <b>Люлько Ярослав Александрович</b>\n"
                         f"- ylyulko@hse.ru\n\n"
                         f"👤 <b>Шелике Аяна Георгиевна</b>\n"
                         f"- ashelike@hse.ru\n\n"
                         f"👤 <b>Житлухин Михаил Валентинович</b>\n"
                         f"- mzhitlukhin@hse.ru\n\n"
                         f"👤 <b>Потапов Денис Игоревич</b>\n"
                         f"- dipotapov@hse.ru"
                         , reply_markup=ikb_SmartLMS_professors_back)

@dp.callback_query_handler(text='SmartLMS_microeconomics_professors')
async def command_microeconomics_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📙 Microeconomics professors:</b>\n\n"
                         f"👤 <b>Юрко Анна Вячеславовна\n</b>"
                         f"- ayurko@hse.ru\n\n"
                         f"👤 <b>Ворчик Андрей Денисович</b>\n"
                         f"- avorchik@hse.ru\n\n"
                         f"👤 <b>Автономов Юрий Владимирович</b>\n"
                         f"- yavtonomov@hse.ru\n\n"
                         f"👤 <b>Верем Ирина Юрьевна</b>\n"
                         f"- iverem@hse.ru\n\n"
                         f"👤 <b>Векилян Армине Вегенаковна</b>\n"
                         f"- avekilyan@hse.ru\n\n"
                         f"👤 <b>Чернышова Яна Алексеевна</b>\n"
                         f"- ychernyshova@hse.ru\n\n"
                         f"👤 <b>Зимрутян Гаянэ Аршаковна</b>\n"
                         f"- gzimrutyan@hse.ru"
                         , reply_markup=ikb_SmartLMS_professors_back)

@dp.callback_query_handler(text='SmartLMS_history_professors')
async def command_history_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📔 History professors:</b>\n\n"
                         f"👤 <b>Царева Александра Петровна</b>\n"
                         f"- atsareva@hse.ru\n\n"
                         f"👤 <b>Отдельнов Марк Михайлович</b>\n"
                         f"- motdelnov@hse.ru\n\n"
                         f"👤 <b>Петрова Мария Святославовна</b>\n"
                         f"- mspetrova@hse.ru\n\n"
                         , reply_markup=ikb_SmartLMS_professors_back)

@dp.callback_query_handler(text='SmartLMS_philosophy_professors')
async def command_philosophy_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📒 Philosophy professors:</b>\n\n"
                         f"👤 <b>Сейрсингх Кристер Раджендра</b>\n"
                         f"- sairsingh@hse.ru\n\n"
                         f"👤 <b>Отдельнов Марк Михайлович</b>\n"
                         f"- motdelnov@hse.ru\n\n"
                         , reply_markup=ikb_SmartLMS_professors_back)

@dp.callback_query_handler(text='SmartLMS_ics_professors')
async def command_ics_professors(call: types.CallbackQuery):
    await call.message.edit_text(f"<b>📓 ICS professors:</b>\n\n"
                         f"👤 <b>Акиншин Анатолий Анатольевич</b>\n"
                         f"- aakinshin@hse.ru\n\n"
                         f"👤 <b>Бессонова Ирина Анатольевна</b>\n"
                         f"- ibes@hse.ru"
                         , reply_markup=ikb_SmartLMS_professors_back)

