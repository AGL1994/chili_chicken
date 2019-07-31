from datetime import datetime

from peewee import *

from db import blog_db


class TimeTag(Model):
    """ 标记 """
    created = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S', verbose_name='创建时间')
    updated = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S', verbose_name='更新时间')
    deleted = IntegerField(default=0, verbose_name='删除标记')

    class Meta:
        database = blog_db


class Serialization:

    def serial(self):
        pass


class BaseModel(TimeTag, Serialization):
    pass
