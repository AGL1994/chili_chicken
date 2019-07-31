# chili_chicken(开发中...)
主要使用sanic、 peewee开发的博客系统
## 主要技术
1. sanic，文档：https://sanic.readthedocs.io/en/latest/
2. （可以替换成自己熟悉ORM框架的异步版本）peewee，官方文档：http://docs.peewee-orm.com/en/latest/
3. peewee-sync 官方文档：https://peewee-async.readthedocs.io/en/latest/
## 项目目录结构
│── models　　　　　　　　　// peewee models存放路径，定义了所有的数据库模型 \
│　│──  __init__.py                                  \
│　│──  base.py　　　　　　// 公共的model \
│　│──  model1.py　　　　　// 其他业务相关model \
│　│──  model2.py　　　　　// 其他业务相关model \
│── views　　　　　　　　　// 项目视图函数文件夹 \
│　│──  __init__.py                                  \
│　│──  view.py　　　　　　// 视图函数文件 \
│── db.py　　　　　　　　　// 数据库配置文件 \
│── server　　　　　　　　　// 项目启动文件 \
│── Pipfile　　　　　　　　　// pipenv文件 \
│── Pipfile.lock　　　　　　　// pipenv文件

## 项目启动
1. 安装依赖请自行搜索Pipenv使用方式，使用pip安装也可以使用项目中的requirement.txt进行安装。
```cython
# 以下列出不同数据库安装的驱动，据官方目前只支持这两种数据库的异步
# 具体参考官方文档：https://peewee-async.readthedocs.io/en/latest/index.html?highlight=aiomysql#install
# PostgreSQL: pip install aiopg
# MySQL: pip install aiomysql
```
2. 启动代码：
```cython
# 数据库配置  db.py
# 数据库使用的是MySQL
import peewee_async
db = {
    'user': 'root',  # 用户名
    'host': '192.168.88.157',  # 数据库地址
    'password': '123456',  # 密码
    'port': 3306,  # 端口
    'max_connections': 10,  # 最大链接数
    'charset': 'utf8mb4',  # 字符集
}
# PooledMySQLDatabase使用链接池，
blog_db = peewee_async.PooledMySQLDatabase('db_name', **db)  # 数据库名
objects = peewee_async.Manager(blog_db)

# 启动项目 server.py
from sanic import Sanic
from views.article import bp as article_bp  # 需要注册的view

app = Sanic()
app.blueprint(article_bp)  # 注册蓝图

# 运行即可
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```