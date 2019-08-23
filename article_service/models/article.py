
import peewee


class ArticleType(peewee.Model):
    """ 文章类型 """
    title = peewee.CharField(max_length=50, verbose_name="名称")
    description = peewee.CharField(max_length=1000, verbose_name="描述")


class Article(peewee.Model):
    """ 文章 """
    author_id = peewee.IntegerField(verbose_name="作者")
    article_type = peewee.ForeignKeyField(ArticleType, verbose_name="文章类型")
    title = peewee.CharField(max_length=100, verbose_name="文章标题")
    content = peewee.TextField(verbose_name="文章内容")
