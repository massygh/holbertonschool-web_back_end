import redis
import uuid
from typing import Union
from functools import wraps


def count_calls(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self = args[0]
        self._redis.rpush(input_key, str(args[1:]))
        output = method(*args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(method):
    r = method.__self__._redis
    name = method.__qualname__
    inputs = r.lrange(f"{name}:inputs", 0, -1)
    outputs = r.lrange(f"{name}:outputs", 0, -1)
    count = r.get(name)
    try:
        count_int = int(count) if count else 0
    except Exception:
        count_int = 0
    print(f"{name} was called {count_int} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{name}(*{inp.decode()}) -> {out.decode()}")

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
