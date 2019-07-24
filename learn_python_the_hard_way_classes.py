
import functools


def decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('hello world')
        result = f(*args, **kwargs)
        return result
    return wrapper


@decorator
def add(a, b):
    print(a + b)

def decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('hello world')
        result = f(*args, **kwargs)
        return result
    return wrapper


@decorator
def add(a, b):
    print(a + b)