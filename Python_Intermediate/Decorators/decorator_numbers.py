def check_numbers(func):
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())

        for value in all_values:
            if type(value) not in (int, float):
                raise TypeError(f"{value} no es un número")

        return func(*args, **kwargs)

    return wrapper


@check_numbers
def numbers(a, b, c):
    return f"{a}, {b}, {c}"


print(numbers(1, 2, c=3))
