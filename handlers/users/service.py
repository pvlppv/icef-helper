from aiogram import types

from data.config import admins
from data.service_config import dir1
from filters import IsPrivateMessage
from loader import dp
import subprocess
import shlex

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc

# def start(bot, update):
@dp.message_handler(IsPrivateMessage(), text='/help', chat_id=admins)
async def command_help(message: types.Message):
    await message.answer('<b>Server commands list:</b>\n\n'
                         '/status - статус сервера\n'
                         '/ifconfig - сетевые настройки\n'
                         '/df - информация о дисковом пространстве (df -h)\n'
                         '/free - информация о памяти\n'
                         '/mpstat - информация о нагрузке на процессор\n'
                         '/dir1 - объём папки + dir1')

#функция команады id
# def myid(bot, update):
#     userid = update.message.from_user.id
#     bot.sendMessage(chat_id=update.message.chat_id, text=userid)

#функция команады ifconfig
@dp.message_handler(IsPrivateMessage(), text='/ifconfig', chat_id=admins)
async def ifconfig(message: types.Message):
    run_command("ifconfig")
    await message.answer(textoutput)

#функция команады df
@dp.message_handler(IsPrivateMessage(), text='/df', chat_id=admins)
async def df(message: types.Message):
    run_command("df -h")
    await message.answer(textoutput)

#функция команады free
@dp.message_handler(IsPrivateMessage(), text='/free', chat_id=admins)
async def free(message: types.Message):
    run_command("free -m")
    await message.answer(textoutput)

#функция команады mpstat
@dp.message_handler(IsPrivateMessage(), text='/mpstat', chat_id=admins)
async def mpstat(message: types.Message):
    run_command("mpstat")
    await message.answer(textoutput)

#функция команады top
@dp.message_handler(IsPrivateMessage(), text='/status', chat_id=admins)
async def apachestatus(message: types.Message):
    run_command("sysmtectl status ICEFHelper.service")
    await message.answer(textoutput)

#функция команады dir1
@dp.message_handler(IsPrivateMessage(), text='/dir1', chat_id=admins)
async def dir1(message: types.Message):
    dir1_command = f'du -sh + {dir1}'
    run_command(dir1_command)
    await message.answer(textoutput)

#функция команады dirbackup - проверяет наличие файла по дате
# def dirbackup(bot, update):
#     reload(config)
#     user = str(update.message.from_user.id)
#     if user in config.admin: #если пользовательский id в списке admin то команда выполняется
#         now_date = datetime.date.today() # Текущая дата
#         cur_year = str(now_date.year) # Год текущий
#         cur_month = now_date.month # Месяц текущий
#         if cur_month < 10:
#             cur_month = str(now_date.month)
#             cur_month = '0'+ cur_month
#         else:
#             cur_month = str(now_date.month)
#         cur_day = str(now_date.day) # День текущий
#         filebackup = config.dir_backup + cur_year + '-' + cur_month + '-' + cur_day + '.03.00.co.7z'  #формируем имя файла для поиска
#         print (filebackup)
#         filebackup_command = "ls -lh "+ filebackup
#         run_command(filebackup_command)
#         bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)



# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# ifconfig_handler = CommandHandler('ifconfig', ifconfig)
# dispatcher.add_handler(ifconfig_handler)
#
# df_handler = CommandHandler('df', df)
# dispatcher.add_handler(df_handler)
#
# free_handler = CommandHandler('free', free)
# dispatcher.add_handler(free_handler)
#
# mpstat_handler = CommandHandler('mpstat', mpstat)
# dispatcher.add_handler(mpstat_handler)
#
# apachestatus_handler = CommandHandler('apachestatus', apachestatus)
# dispatcher.add_handler(apachestatus_handler)
#
# dir1_handler = CommandHandler('dir1', dir1)
# dispatcher.add_handler(dir1_handler)

# dirbackup_handler = CommandHandler('dirbackup', dirbackup)
# dispatcher.add_handler(dirbackup_handler)

# myid_handler = CommandHandler('id', myid)
# dispatcher.add_handler(myid_handler)
#
# help_handler = CommandHandler('help', help)
# dispatcher.add_handler(help_handler)