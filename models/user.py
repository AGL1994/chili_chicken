import peewee

from models.base import BaseModel


class User(BaseModel):
    """ 用户 """
    username = peewee.CharField(max_length=50, verbose_name="用户名")
    password = peewee.CharField(max_length=20, verbose_name="密码")
