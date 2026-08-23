from datetime import datetime


def validate_numbers(func):
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())
        for value in all_values:
            if type(value) not in (int, float):
                raise ValueError("El dato ingresado no es un numero")

        return func(*args, **kwargs)

    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(
            f"func:{func.__name__} - args: {args} - [{datetime.now()}] -"f" Resultado: {result}")

        print(f"Resultado {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return (a*b)


multiply(3, 4)
