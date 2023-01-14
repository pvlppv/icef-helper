from gino import Gino
import sqlalchemy as sa
from typing import List
import datetime
from aiogram import Dispatcher
from sqlalchemy import Column, DateTime, func

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.datetime.utcnow, server_default=func.now())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, server_default=func.now())



async def on_startup(dispatcher: Dispatcher):
    print('PostgreSQL was connected.')
    await db.set_bind(config.POSTGRES_URI)
