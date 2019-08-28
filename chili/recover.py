
from sanic import Blueprint


# class RegisterProxy:
#
#     def __init__(self, function, cls, method):
#         self.function = function
#         self.method = method
#         self.cls = cls
#
#     def register_proxy(self, uri, *args, **kwargs):
#
#         return self.function(uri, *args, **kwargs)
#
#
# class RecoverBlueprintMetaclass(type):
#     register_methods = ('route', )
#
#     def __new__(mcls, name, bases, attrs, **kwargs):
#         cls = super().__new__(mcls, name, bases, attrs, **kwargs)
#
#         for method in mcls.register_methods:
#             if hasattr(cls, method):
#                 proxy = RegisterProxy(getattr(cls, method), cls, method)
#                 setattr(cls, method, proxy.register_proxy)
#         return cls
#
#
# class RBlueprint(Blueprint, metaclass=RecoverBlueprintMetaclass):
#     pass

class RBlueprint(Blueprint):

    def route(
        self,
        uri,
        methods=frozenset({"GET"}),
        **kwargs
    ):
        """ 注册地址 """
        print('======')
        return super().route(uri, methods=methods, **kwargs)


