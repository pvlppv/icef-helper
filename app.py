import asyncio

from handlers.users.morning import scheduler_morning
from handlers.users.schedule_subjects import scheduler_subjects


async def on_startup(dp):

    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Connecting to PostgreSQL.')
    await on_startup(dp)

    # print('Deleting of database.')
    # await db.gino.drop_all()

    print('Creating a table.')
    await db.gino.create_all()
    print('Done.')

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    # from utils.set_bot_commands import set_default_commands
    # await set_default_commands(dp)

    asyncio.create_task(scheduler_morning())
    asyncio.create_task(scheduler_subjects())

    print('ICEF Helper is on.')

async def on_shutdown(dp):

    from utils.notify_admins import on_shotdown_notify
    await on_shotdown_notify(dp)
    print('ICEF Helper is off.')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)