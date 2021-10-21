def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() returned {original_result}')

        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'

say('Bob', 'Hello underworld')
