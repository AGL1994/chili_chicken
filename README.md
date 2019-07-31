# chili_chicken
主要使用sanic、 peewee开发的博客系统
## 项目目录结构
│── models                               // peewee models存放路径，定义了所有的数据库模型 \
│　│──  __init__.py                                  \
│　│──  base.py                         // 公共的model \
│　│──  model1.py                       // 其他业务相关model \
│　│──  model2.py                       // 其他业务相关model \
│── views                                // 项目视图函数文件夹 \
│　│──  __init__.py                                  \
│　│──  view.py                         // 视图函数文件 \
│── db.py                                // 数据库配置文件 \
│── server                               // 项目启动文件 \
│── Pipfile                              // pipenv文件 \
│── Pipfile.lock                         // pipenv文件