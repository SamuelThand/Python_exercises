#Decorators


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'{prefix} Executed before {original_function.__name__}')
            result = original_function(*args, **kwargs)
            print(f'{prefix} Executed after {original_function.__name__}')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('abc')
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('disp;', 33)