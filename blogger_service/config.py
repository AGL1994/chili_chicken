import threading

from blogger_service import SERVICE_NAME
from chili import gateway


# class Config(gateway.BaseConfig):
#
#     def __init__(self):
#         super().__init__(SERVICE_NAME)
#
#
#
#     _instance_lock = threading.Lock()
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Config, "_instance"):
#             with Config._instance_lock:
#                 if not hasattr(Config, "_instance"):
#                     Config._instance = object.__new__(cls)
#         return Config._instance
