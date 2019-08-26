from collections import defaultdict

from sanic import Blueprint


class RegisterProxy:

    def __init__(self, function, cls, method):
        self.function = function
        self.method = method
        self.cls = cls

    def register_proxy(self, uri, *args, **kwargs):
        # print(self.cls)
        # print(self.method)
        dd = self.function
        print(id(self.cls))
        # return self.function(self.cls, uri, *args, **kwargs)
        function = getattr(self.cls, 'b' + self.method)
        return function(uri, *args, **kwargs)


def ll(function, *args, **kwargs):
    return function(*args, **kwargs)


class RecoverBlueprintMetaclass(type):
    register_methods = ('get', 'post', 'put', 'delete', 'route')

    def __new__(mcls, name, bases, attrs, **kwargs):
        # print(hasattr(mcls, 'strict_slashes'))
        cls = super().__new__(mcls, name, bases, attrs, **kwargs)

        for method in mcls.register_methods:
            if hasattr(cls, method):
                # print(hasattr(cls, 'strict_slashes'))
                # print(id(cls))
                setattr(cls, 'b' + method, getattr(cls, method))
                proxy = RegisterProxy(getattr(cls, method), cls, method)
        #
                setattr(cls, method, proxy.register_proxy)
        return cls


class RBlueprint(Blueprint, metaclass=RecoverBlueprintMetaclass):
    pass


