def first_decorator(func):

    def wrapper(*args, **kwargs):
        print(f"Parámetros: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Retorno: {result}")
        return result

    return wrapper


@first_decorator
def greetings(hello, world):
    return f"{hello} {world}"


greetings("hola", world="mundo")
