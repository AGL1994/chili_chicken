import peewee

from blogger_service.db import blog_db


class User(peewee.Model):
    """ 用户 """
    username = peewee.CharField(max_length=50, verbose_name="用户名")
    password = peewee.CharField(max_length=20, verbose_name="密码")

    class Meta:
        database = blog_db
