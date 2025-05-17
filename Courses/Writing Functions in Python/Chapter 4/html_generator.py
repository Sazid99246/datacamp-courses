def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<b>{}</b>'.format(msg)
    return wrapper


def italics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<i>{}</i>'.format(msg)
    return wrapper


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)
        return wrapper
    return decorator


@html('<b>', '</b>')
def hello(name):
    return 'Hello {}!'.format(name)


print(hello('Alice'))


@html('<i>', '</i>')
def goodbye(name):
    return 'Goodbye {}.'.format(name)


print(goodbye('Alice'))


@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))
