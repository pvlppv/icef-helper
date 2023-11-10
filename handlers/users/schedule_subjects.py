import asyncio
import json
import calendar
import datetime
from datetime import date, datetime, timedelta
from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty
from collections import defaultdict
import aioschedule

from keyboards.inline.inline_keyboard_schedule import ikb_schedule_calculus_back, ikb_schedule_statistics_back, \
    ikb_schedule_microeconomics_back, ikb_schedule_history_back, ikb_schedule_philosophy_back, ikb_schedule_ics_back
from keyboards.inline.inline_keyboard_schedule_subjects import ikb_schedule_microeconomics, ikb_schedule_subjects, \
    ikb_schedule_calculus, ikb_schedule_statistics, ikb_schedule_ics, ikb_schedule_philosophy, ikb_schedule_history
from loader import dp, db_sql
from filters import IsPrivateMessage, IsDatabaseUserMessage, IsAcceptedUserMessage, \
    IsSubscriberChannelMessage

import ruz

async def schedule_subjects():
    try:
        schedule1 = ruz.person_lessons(email='dskim_2@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule2 = ruz.person_lessons(email='syashlyapochnik@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule3 = ruz.person_lessons(email='osbovbley@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule4 = ruz.person_lessons(email='sikruglov@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule5 = ruz.person_lessons(email='agshirokov@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule6 = ruz.person_lessons(email='eastryukov@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule7 = ruz.person_lessons(email='pgpopov_1@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule8 = ruz.person_lessons(email='aatoktomambetov@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule9 = ruz.person_lessons(email='mvchishko@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule10 = ruz.person_lessons(email='mvpushkarskaya@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        schedule11 = ruz.person_lessons(email='vsmarinkevich@edu.hse.ru', from_date=f'{date.today()}', to_date=f'{date.today() + timedelta(days=7)}')
        for elements in schedule1:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 1'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule2:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 2'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule3:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 3'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule4:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 4'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule5:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 5'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule6:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 6'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule7:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 7'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule8:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 8'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule9:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 9'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule10:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 10'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
        for elements in schedule11:
            date1 = elements.get('date')
            datetimeobject = datetime.strptime(date1, '%Y.%m.%d')
            date2 = f'{datetimeobject.strftime("%d.%m")}, {calendar.day_name[datetimeobject.weekday()]}'
            begin_lesson = elements.get('beginLesson')
            end_lesson = elements.get('endLesson')
            time = f'{begin_lesson}-{end_lesson}'
            title = elements.get('discipline')
            professor = elements.get('lecturer_title')
            auditorium = elements.get('auditorium')
            group = 'Group 11'
            db_sql.add_subjects_schedule(date2, time, title, professor, auditorium, group)
    except MessageTextIsEmpty:
        pass

@dp.callback_query_handler(text='schedule_subjects')
async def command_subjects_schedule(call: types.CallbackQuery):
    await call.message.edit_text('<b>📚 Subjects schedule:</b>', reply_markup=ikb_schedule_subjects)

@dp.callback_query_handler(text='schedule_subjects_back')
async def command_schedule_subjects_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📚 Subjects schedule:</b>', reply_markup=ikb_schedule_subjects)

@dp.callback_query_handler(text='schedule_calculus')
async def command_schedule_calculus(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus schedule:</b>', reply_markup=ikb_schedule_calculus)

@dp.callback_query_handler(text='schedule_statistics')
async def command_schedule_statistics(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics schedule:</b>', reply_markup=ikb_schedule_statistics)

@dp.callback_query_handler(text='schedule_microeconomics')
async def command_schedule_microeconomics(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics schedule:</b>', reply_markup=ikb_schedule_microeconomics)

@dp.callback_query_handler(text='schedule_history')
async def command_schedule_historyy(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History schedule:</b>', reply_markup=ikb_schedule_history)

@dp.callback_query_handler(text='schedule_philosophy')
async def command_schedule_philosophy(call: types.CallbackQuery):
    await call.message.edit_text('<b>📒 Philosophy schedule:</b>', reply_markup=ikb_schedule_philosophy)

@dp.callback_query_handler(text='schedule_ics')
async def command_schedule_ics(call: types.CallbackQuery):
    await call.message.edit_text('<b>📓 ICS schedule:</b>', reply_markup=ikb_schedule_ics)

@dp.callback_query_handler(text='schedule_calculus_back')
async def command_schedule_calculus_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📘 Calculus schedule:</b>', reply_markup=ikb_schedule_calculus)

@dp.callback_query_handler(text='schedule_statistics_back')
async def command_schedule_statistics_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📗 Statistics schedule:</b>', reply_markup=ikb_schedule_statistics)

@dp.callback_query_handler(text='schedule_microeconomics_back')
async def command_schedule_microeconomics_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📙 Microeconomics schedule:</b>', reply_markup=ikb_schedule_microeconomics)

@dp.callback_query_handler(text='schedule_history_back')
async def command_schedule_history_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📔 History schedule:</b>', reply_markup=ikb_schedule_history)

@dp.callback_query_handler(text='schedule_philosophy_back')
async def command_schedule_philosophy_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📒 Philosophy schedule:</b>', reply_markup=ikb_schedule_philosophy)

@dp.callback_query_handler(text='schedule_ics_back')
async def command_schedule_ics_back(call: types.CallbackQuery):
    await call.message.edit_text('<b>📓 ICS schedule:</b>', reply_markup=ikb_schedule_ics)



@dp.callback_query_handler(text='schedule_calculus_monday')
async def schedule_calculus_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for monday.</b>', reply_markup=ikb_schedule_calculus_back)
@dp.callback_query_handler(text='schedule_calculus_tuesday')
async def schedule_calculus_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for tuesday.</b>', reply_markup=ikb_schedule_calculus_back)
@dp.callback_query_handler(text='schedule_calculus_wednesday')
async def schedule_calculus_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for wednesday.</b>', reply_markup=ikb_schedule_calculus_back)
@dp.callback_query_handler(text='schedule_calculus_thursday')
async def schedule_calculus_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for thursday.</b>', reply_markup=ikb_schedule_calculus_back)
@dp.callback_query_handler(text='schedule_calculus_friday')
async def schedule_calculus_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for friday.</b>', reply_markup=ikb_schedule_calculus_back)
@dp.callback_query_handler(text='schedule_calculus_saturday')
async def schedule_calculus_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="Математический анализ (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_calculus_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📘 No calculus for saturday.</b>', reply_markup=ikb_schedule_calculus_back)

@dp.callback_query_handler(text='schedule_statistics_monday')
async def schedule_statistics_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for monday.</b>', reply_markup=ikb_schedule_statistics_back)
@dp.callback_query_handler(text='schedule_statistics_tuesday')
async def schedule_statistics_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for tuesday.</b>', reply_markup=ikb_schedule_statistics_back)
@dp.callback_query_handler(text='schedule_statistics_wednesday')
async def schedule_statistics_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for wednesday.</b>', reply_markup=ikb_schedule_statistics_back)
@dp.callback_query_handler(text='schedule_statistics_thursday')
async def schedule_statistics_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for thursday.</b>', reply_markup=ikb_schedule_statistics_back)
@dp.callback_query_handler(text='schedule_statistics_friday')
async def schedule_statistics_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for friday.</b>', reply_markup=ikb_schedule_statistics_back)
@dp.callback_query_handler(text='schedule_statistics_saturday')
async def schedule_statistics_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="Теория вероятностей и статистика (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_statistics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📗 No statistics for saturday.</b>', reply_markup=ikb_schedule_statistics_back)

@dp.callback_query_handler(text='schedule_microeconomics_monday')
async def schedule_microeconomics_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for monday.</b>', reply_markup=ikb_schedule_microeconomics_back)
@dp.callback_query_handler(text='schedule_microeconomics_tuesday')
async def schedule_microeconomics_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for tuesday.</b>', reply_markup=ikb_schedule_microeconomics_back)
@dp.callback_query_handler(text='schedule_microeconomics_wednesday')
async def schedule_microeconomics_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for wednesday.</b>', reply_markup=ikb_schedule_microeconomics_back)
@dp.callback_query_handler(text='schedule_microeconomics_thursday')
async def schedule_microeconomics_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for thursday.</b>', reply_markup=ikb_schedule_microeconomics_back)
@dp.callback_query_handler(text='schedule_microeconomics_friday')
async def schedule_microeconomics_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for friday.</b>', reply_markup=ikb_schedule_microeconomics_back)

@dp.callback_query_handler(text='schedule_microeconomics_saturday')
async def schedule_microeconomics_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="Основы микроэкономики (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_microeconomics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📙 No microeconomics for saturday.</b>', reply_markup=ikb_schedule_microeconomics_back)

@dp.callback_query_handler(text='schedule_history_monday')
async def schedule_history_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for monday.</b>', reply_markup=ikb_schedule_history_back)
@dp.callback_query_handler(text='schedule_history_tuesday')
async def schedule_history_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for tuesday.</b>', reply_markup=ikb_schedule_history_back)
@dp.callback_query_handler(text='schedule_history_wednesday')
async def schedule_history_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for wednesday.</b>', reply_markup=ikb_schedule_history_back)
@dp.callback_query_handler(text='schedule_history_thursday')
async def schedule_history_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for thursday.</b>', reply_markup=ikb_schedule_history_back)
@dp.callback_query_handler(text='schedule_history_friday')
async def schedule_history_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for friday.</b>', reply_markup=ikb_schedule_history_back)
@dp.callback_query_handler(text='schedule_history_saturday')
async def schedule_history_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="Мировая интеллектуальная история (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_history_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📔 No history for saturday.</b>', reply_markup=ikb_schedule_history_back)

@dp.callback_query_handler(text='schedule_philosophy_monday')
async def schedule_philosophy_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for monday.</b>', reply_markup=ikb_schedule_philosophy_back)
@dp.callback_query_handler(text='schedule_philosophy_tuesday')
async def schedule_philosophy_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for tuesday.</b>', reply_markup=ikb_schedule_philosophy_back)
@dp.callback_query_handler(text='schedule_philosophy_wednesday')
async def schedule_philosophy_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for wednesday.</b>', reply_markup=ikb_schedule_philosophy_back)
@dp.callback_query_handler(text='schedule_philosophy_thursday')
async def schedule_philosophy_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for thursday.</b>', reply_markup=ikb_schedule_philosophy_back)
@dp.callback_query_handler(text='schedule_philosophy_friday')
async def schedule_philosophy_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for friday.</b>', reply_markup=ikb_schedule_philosophy_back)
@dp.callback_query_handler(text='schedule_philosophy_saturday')
async def schedule_philosophy_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="История западной философии (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_philosophy_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📒 No philosophy for saturday.</b>', reply_markup=ikb_schedule_philosophy_back)

@dp.callback_query_handler(text='schedule_ics_monday')
async def schedule_ics_monday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_monday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for monday.</b>', reply_markup=ikb_schedule_ics_back)
@dp.callback_query_handler(text='schedule_ics_tuesday')
async def schedule_ics_tuesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_tuesday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for tuesday.</b>', reply_markup=ikb_schedule_ics_back)
@dp.callback_query_handler(text='schedule_ics_wednesday')
async def schedule_ics_wednesday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_wednesday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for wednesday.</b>', reply_markup=ikb_schedule_ics_back)
@dp.callback_query_handler(text='schedule_ics_thursday')
async def schedule_ics_thursday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_thursday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for thursday.</b>', reply_markup=ikb_schedule_ics_back)
@dp.callback_query_handler(text='schedule_ics_friday')
async def schedule_ics_friday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_friday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for friday.</b>', reply_markup=ikb_schedule_ics_back)
@dp.callback_query_handler(text='schedule_ics_saturday')
async def schedule_ics_saturday(call: types.CallbackQuery):
    try:
        data = db_sql.subjects_schedule_saturday(title="Информационные компьютерные системы (анг)")
        values = ''
        for value in data:
            values += f'<b><ins>📍 {value[0]}</ins></b>\n\n'
            break
        for value in data:
            values += f'<b>🕓 {value[1]}</b>\n' \
                      f'<b>{value[2]}</b>\n' \
                      f'{value[3]}\n' \
                      f'{value[5]}\n' \
                      f'<b>{value[4]}</b>\n\n'
        await call.message.edit_text(values, reply_markup=ikb_schedule_ics_back)
    except MessageTextIsEmpty:
        await call.message.edit_text('<b>📓 No ICS for saturday.</b>', reply_markup=ikb_schedule_ics_back)




async def scheduler_subjects():
    aioschedule.every().monday.at('00:00').do(schedule_subjects)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

