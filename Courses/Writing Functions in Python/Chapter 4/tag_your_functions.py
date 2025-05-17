from functools import wraps


def tag(*tags):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass


print(foo.tags)
