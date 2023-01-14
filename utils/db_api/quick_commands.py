from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.users import User



async def new_user(user_id: int, username: str, name: str, course: int, academic_group: int, specialization: str, additional_courses: str, sport: str, email: str, status: str):
    try:
        user = User(user_id=user_id, name=name, username=username, course=course, academic_group=academic_group, specialization=specialization, additional_courses=additional_courses, sport=sport, email=email, status=status)
        await user.create()
    except UniqueViolationError:
        print('User was not created.')

async def select_all_users():
    users = await User.query.gino.all()
    return users

async def delete_user(name):
    name = await User.delete.where(User.name == name).gino.status()
    return name

async def count_users_1course():
    count = await (db.select([db.func.count()]).where(User.course == 1).gino.scalar())
    return count

async def count_users_2course():
    count = await (db.select([db.func.count()]).where(User.course == 2).gino.scalar())
    return count

async def count_users_3course():
    count = await (db.select([db.func.count()]).where(User.course == 3).gino.scalar())
    return count

async def count_users_4course():
    count = await (db.select([db.func.count()]).where(User.course == 4).gino.scalar())
    return count

async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

# editing profile

async def select_user_name(name):
    name = await User.query.where(User.name == name).gino.first()
    return name

async def select_user_username(username):
    username = await User.query.where(User.name == username).gino.first()
    return username

async def select_user_course(course):
    course = await User.query.where(User.user_id == course).gino.first()
    return course

async def select_user_academic_group(academic_group):
    academic_group = await User.query.where(User.user_id == academic_group).gino.first()
    return academic_group

async def select_user_specialization(specialization):
    specialization = await User.query.where(User.user_id == specialization).gino.first()
    return specialization

async def select_user_additional_courses(additional_courses):
    additional_courses = await User.query.where(User.user_id == additional_courses).gino.first()
    return additional_courses

async def select_user_created_at(created_at):
    created_at = await User.query.where(User.user_id == created_at).gino.first()
    return created_at

async def select_user_sport(sport):
    sport = await User.query.where(User.user_id == sport).gino.first()
    return sport

async def select_user_email(email):
    email = await User.query.where(User.user_id == email).gino.first()
    return email

# morning
async def select_user_morning_status(morning_status):
    morning_status = await User.query.where(User.user_id == morning_status).gino.first()
    return morning_status

async def select_morning_status_on():
    morning_status = await User.query.where(User.morning_status == 'On').gino.first()
    return morning_status


# async def select_notification_status_limited():
#     notification_status = await User.query.where(User.notification_status == 'Limited').gino.first()
#     return notification_status

async def select_morning_status_off():
    morning_status = await User.query.where(User.morning_status == 'Off').gino.first()
    return morning_status

async def select_user_morning_time(morning_time):
    morning_time = await User.query.where(User.user_id == morning_time).gino.first()
    return morning_time
# notifications
async def select_user_notification_status(notification_status):
    notification_status = await User.query.where(User.user_id == notification_status).gino.first()
    return notification_status

async def select_notification_status_on():
    notification_status = await User.query.where(User.notification_status == 'On').gino.first()
    return notification_status

# async def select_notification_status_limited():
#     notification_status = await User.query.where(User.notification_status == 'Limited').gino.first()
#     return notification_status

async def select_notification_status_off():
    notification_status = await User.query.where(User.notification_status == 'Off').gino.first()
    return notification_status

# additional courses search
async def select_profile_additional_courses_python():
    additional_courses = await User.query.where(User.additional_courses >= 'Python').gino.all()
    return additional_courses
async def select_profile_additional_courses_excel():
    additional_courses = await User.query.where(User.additional_courses >= 'Excel').gino.all()
    return additional_courses
async def select_profile_additional_courses_trading():
    additional_courses = await User.query.where(User.additional_courses >= 'Trading').gino.all()
    return additional_courses
async def select_profile_additional_courses_music():
    additional_courses = await User.query.where(User.additional_courses >= 'Music').gino.all()
    return additional_courses
async def select_profile_additional_courses_french():
    additional_courses = await User.query.where(User.additional_courses >= 'French').gino.all()
    return additional_courses
async def select_profile_additional_courses_italian():
    additional_courses = await User.query.where(User.additional_courses >= 'Italian').gino.all()
    return additional_courses
async def select_profile_additional_courses_deutsch():
    additional_courses = await User.query.where(User.additional_courses >= 'Deutsch').gino.all()
    return additional_courses
async def select_profile_additional_courses_spanish():
    additional_courses = await User.query.where(User.additional_courses >= 'Spanish').gino.all()
    return additional_courses
async def select_profile_additional_courses_chinese():
    additional_courses = await User.query.where(User.additional_courses >= 'Chinese').gino.all()
    return additional_courses
async def select_profile_additional_courses_arabic():
    additional_courses = await User.query.where(User.additional_courses >= 'Arabic').gino.all()
    return additional_courses
async def select_profile_additional_courses_gym():
    additional_courses = await User.query.where(User.additional_courses >= 'Gym').gino.all()
    return additional_courses
async def select_profile_additional_courses_yoga():
    additional_courses = await User.query.where(User.additional_courses >= 'Yoga').gino.all()
    return additional_courses

# specialization search
async def select_profile_specialization_bdf():
    specialization = await User.query.where(User.specialization == 'Банковское дело и финансы').gino.all()
    return specialization
async def select_profile_specialization_emanage():
    specialization = await User.query.where(User.specialization == 'Экономика и менеджмент').gino.all()
    return specialization
async def select_profile_specialization_e():
    specialization = await User.query.where(User.specialization == 'Экономика').gino.all()
    return specialization
async def select_profile_specialization_ef():
    specialization = await User.query.where(User.specialization == 'Экономика и финансы').gino.all()
    return specialization
async def select_profile_specialization_buf():
    specialization = await User.query.where(User.specialization == 'Бухгалтерский учёт и финансы').gino.all()
    return specialization
async def select_profile_specialization_emath():
    specialization = await User.query.where(User.specialization == 'Экономика и математика').gino.all()
    return specialization



# accepting registration
async def select_unregistered():
    status = await User.query.where(User.status == 'None').gino.first()
    return status

async def accept_registration(user_id: int):
    registration = await select_user(user_id)
    await registration.update(status='Accepted').apply()

async def delete_user_and_registration(user_id: int):
    user_id = await User.delete.where(User.user_id == user_id).gino.status()
    return user_id

async def select_users_all():
    user_id = await User.select('user_id').gino.all()
    return user_id

