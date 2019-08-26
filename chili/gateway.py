import asyncio
import threading

import aiohttp
import requests

from chili import error


async def do_request(url, method='get', params=None, json=None):
    """ 异步post """
    async with aiohttp.ClientSession() as session:
        async with getattr(session, method)(url, params=params, json=json) as response:
            return await response_result(response)


async def response_result(response):
    """ 异步返回参数 """
    return {
        'status': response.status,
        'result': await response.text()
    }


def sync_get(url, headers=None):
    """ 同步get """
    if headers is None:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = requests.get(url=url, headers=headers)
    return data.json()


async def get_service_function(service_name, function_name):
    """ 通过服务名称与方法名称获取完整的url """
    # 此处与服务注册发现相关
    uri = 'http://127.0.0.1:8002'
    path = '/blogger'
    return uri, path


class ServiceClient:
    """ 调用其他服务类 """
    methods = ('get', 'post', 'put', 'delete')

    async def transfer_service(self, service_name, function_name, method='get', *args, **kwargs):
        """ 实际调用方法 """
        if method in self.methods:
            uri, path = await get_service_function(service_name, function_name)
            params = kwargs.get('params', None)
            json = kwargs.get('json', None)
            return await do_request(uri + path, method=method, params=params, json=json)
        else:
            raise error.GatewayMethodNotFoundError(f'请求方法不存在，期望方法：{method}，允许方法：{self.methods}')


def service_client(service_name, function_name, method=None):
    """
    调用服务装饰器
    :param method: 请求方法
    :param service_name: 服务名称
    :param function_name: 服务下的接口名称
    :return: {'status': '服务返回状态', 'result': '服务返回结果'}
    """
    def __service(function):
        async def service_client_handler(obj, *args, **kwargs):
            return await obj.transfer_service(service_name, function_name, *args, method=method, **kwargs)
        return service_client_handler
    return __service


class BaseConfig:
    url = 'http://127.0.0.1:8001/config-center'

    def __init__(self, service_name):
        self.service = service_name

    def _get_config(self, name):
        config = sync_get(f'{self.url}/{name}/{self.service}')
        if config:
            return config
        else:
            raise error.ConfigNameNotFoundError(f'配置{name}找不到')

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(BaseConfig, "_instance"):
            with BaseConfig._instance_lock:
                if not hasattr(BaseConfig, "_instance"):
                    BaseConfig._instance = object.__new__(cls)
        return BaseConfig._instance

    def get_db_config(self):
        """ 获取数据库配置 """
        return self._get_config('DATABASE')


