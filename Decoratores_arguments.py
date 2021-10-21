def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@proxy
def greet(*args):
    print(args)

greet('abc')