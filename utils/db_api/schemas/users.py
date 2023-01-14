
from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(200))
    name = Column(String(200))
    course = Column(BigInteger)
    academic_group = Column(BigInteger)
    english_group = Column(BigInteger)
    specialization = Column(String(200))
    additional_courses = Column(String (300))
    sport = Column(String (200))
    status = Column(String(200))
    notification_status = Column(String(200))
    email = Column(String(200))
    morning_status = Column(String(200))
    morning_time = Column(String(200))



    query: sql.select