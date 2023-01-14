import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    384993580,
]

moderators = [
    384993580,
    1077180787
]
# me - 384993580
# 2 acc - 5432466949
# katya - 1077180787

admin = 384993580

first_subscribers = [

]

channels = [
    ['Channel 1', '', '']
]

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'