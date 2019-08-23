import threading

from blogger_service import SERVICE_NAME
from chili import gateway


class Config(gateway.BaseConfig):

    def __init__(self):
        super().__init__(SERVICE_NAME)

    def get_db_config(self):
        """ 获取数据库配置 """
        return self._get_config('DATABASE')

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Config, "_instance"):
            with Config._instance_lock:
                if not hasattr(Config, "_instance"):
                    Config._instance = object.__new__(cls)
        return Config._instance
