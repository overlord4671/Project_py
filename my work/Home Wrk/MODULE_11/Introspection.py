from pprint import pprint
import requests
import time


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = []
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith('__'):
            attributes.append(attr)
    info['attributes'] = attributes

    methods = []
    for method in dir(obj):
        if callable(getattr(obj, method)) and not method.startswith('__'):
            methods.append(method)
    info['methods'] = methods

    info['module'] = obj.__class__.__module__

    if obj in [requests.get, requests.post, requests.put, requests.delete, requests.patch, requests.head,
               requests.options]:
        info['http_method'] = obj.__name__.upper()
    else:
        info['http_method'] = None

    return info


class Exemple:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def exemple(self):
        x = self.a + self.b


start = time.time()
pprint(introspection_info(1))
pprint(introspection_info(Exemple(1, 2)))
end = time.time()
print(f"{end - start:.4f}")
