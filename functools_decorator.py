import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """This docstring gets carried to new decorated function
    when using functools.wraps() function"""
    return 'Hello!'

print(greet.__doc__)
