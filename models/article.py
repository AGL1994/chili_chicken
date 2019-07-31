from models.base import BaseModel
import peewee

from models.user import User


class ArticleType(BaseModel):
    """ 文章类型 """
    title = peewee.CharField(max_length=50, verbose_name="名称")
    description = peewee.CharField(max_length=1000, verbose_name="描述")


class Article(BaseModel):
    """ 文章 """
    author = peewee.ForeignKeyField(User, verbose_name="作者")
    article_type = peewee.ForeignKeyField(ArticleType, verbose_name="文章类型")
    title = peewee.CharField(max_length=100, verbose_name="文章标题")
    content = peewee.TextField(verbose_name="文章内容")
