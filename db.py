from collections import Iterable

import peewee_async
from playhouse.shortcuts import model_to_dict

db = {
    'user': 'root',
    'host': '192.168.88.157',
    'password': '123456',
    'port': 3306,
    'max_connections': 10,
    'charset': 'utf8mb4',
}
blog_db = peewee_async.PooledMySQLDatabase('chili_chicken', **db)
objects = peewee_async.Manager(blog_db)


def models_to_dict(models, *args, **kwargs):
    """ 批量序列化 """
    if not isinstance(models, Iterable):
        return []
    return [
        model_to_dict(model, *args, **kwargs) for model in models
    ]
