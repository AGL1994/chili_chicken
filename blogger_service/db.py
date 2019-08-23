from collections import Iterable

import peewee_async
from playhouse.shortcuts import model_to_dict

from blogger_service.config import Config

database = Config().get_db_config()
print(database)

db_name = database.pop('db_name')
blog_db = peewee_async.PooledMySQLDatabase(db_name, **database)
objects = peewee_async.Manager(blog_db)


def models_to_dict(models, *args, **kwargs):
    """ 批量序列化 """
    if not isinstance(models, Iterable):
        return []
    return [
        model_to_dict(model, *args, **kwargs) for model in models
    ]



