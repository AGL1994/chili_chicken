# chili_chicken(基于sanic开发的异步微服务框架)
### 说明
持续开发中，前期主要自己开发组件，后期会集成现有第三方组件（比如：Consul、Eureka、zk、Kafka等等） \
由于主要框架是现学现卖，对微服务的理解并不深入，有什么错误或者不当的地方望大佬指出。\
项目未进过测试，仅供学习使用 
### 主要技术
1. sanic，文档：https://sanic.readthedocs.io/en/latest/
2. （可以替换成自己熟悉ORM框架的异步版本）peewee，官方文档：http://docs.peewee-orm.com/en/latest/
3. peewee-sync 官方文档：https://peewee-async.readthedocs.io/en/latest/
4. aiohttp 调用其他服务
## 项目目录结构(待完善)
│── blogger_service　　　　　　　　　// 各个微服务  xxx_service \
│　│──  __init__.py                                  \
│　│──  interface　　　　　　// 调用其他微服务的接口 \
│　│  │── __init__.py      // 注册所有接口  \
│　│  │── article.py      // 接口文件
│　│──  models　　　　　// 其他业务相关models \
│　│──  views.py　　　　　// 视图文件 \
│── chili　　　　　　　　　// 服务核心模块，包含了需要的各个组件 \
│　│──  __init__.py                                  \
│　│──  error.py　　　　　　// 相关异常 \
│　│──  gateway.py　　　　　　// 接口相关模块 \
│── config_center　　　　　　　　// 配置中心 \
│── server　　　　　　　　　// 项目启动文件 \
│── Pipfile　　　　　　　　　// pipenv文件 \
│── Pipfile.lock　　　　　　　// pipenv文件

### 各个服务  xxx_service
#### 启动方法
运行 xxx_service/server.py
#### 数据库文件说明 xxx_service/db.py
```cython
from blogger_service import config  # 详细见下config.py说明
import peewee_async

database = config.Config().get_db_config()  # 从配置中心获取数据库配置

# 注册数据库
db_name = database.pop('db_name')
blog_db = peewee_async.PooledMySQLDatabase(db_name, **database)
objects = peewee_async.Manager(blog_db)
```
#### 配置文件说明 xxx_service/config.py
```cython
import threading

from blogger_service import SERVICE_NAME
from chili import gateway  # 详见 chili/gateway.py说明


class Config(gateway.BaseConfig):

    def __init__(self):
        super().__init__(SERVICE_NAME)

    def get_db_config(self):
        """ 获取数据库配置 """
        return self._get_config('DATABASE')
    
    def get_config_name(self):
        """ 需要什么配置文件就写什么方法 """
        return self._get_config('CONFIG_NAME')
    
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Config, "_instance"):
            with Config._instance_lock:
                if not hasattr(Config, "_instance"):
                    Config._instance = object.__new__(cls)
        return Config._instance
```
#### 调用其他服务  
article_service/interface/*.py
```cython
from chili.gateway import ServiceClient, service_client  # 详见 chili/gateway.py说明


class ArticleClient(ServiceClient):

    @service_client('service_name', 'function_name', method='post')  # 需调用的服务名、接口名、method
    async def get_blogger_list(self, json=None):  # json需要传json数据
        """ 获取所有博客用户 """
        pass
```
实际调用 article_service/views/*.py
```cython
from sanic import Blueprint
from sanic.response import json

from article_service import interface

bp = Blueprint(__name__)
article_interface = interface.ArticleClient()  # 需调用的服务接口（上一步定义的方法）


@bp.route('/article')
async def test(request):
    json_params = {'f': 'ff'}
    result = await article_interface.get_blogger_list(json=json_params)  # 调用相关服务方法
    print(result)
    return json({'data': result['result']})
```


### 配置中心 config_center
#### 启动方法
运行 config_center/server.py
#### config.py说明
```cython
CONFIG_NAME = {
    '服务名': {
        'user': '数据库用户',  # must
        'host': '数据库地址',  # must
        'password': '数据库密码',  # must
        'port': '数据库端口',  # must
        'max_connections': '数据库最大连接数',  # not must
        'charset': '字符编码',  # must
        'db_name': '数据库名'  # must
    }
}
# 例如
# 数据库配置
DATABASE = {
    'blogger': {
        'user': 'root',
        'host': '192.168.88.157',
        'password': '123456',
        'port': 3306,
        'max_connections': 10,
        'charset': 'utf8mb4',
        'db_name': 'chili_chicken'
    },
    'article': {
        'user': 'root',
        'host': '192.168.88.157',
        'password': '123456',
        'port': 3306,
        'max_connections': 10,
        'charset': 'utf8mb4',
        'db_name': 'chili_chicken'
    },
}
```
### 下一步 服务注册于发现