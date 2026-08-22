class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        current_year = 2026
        return current_year - self.date_of_birth


def is_adult(func):
    def wrapped(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError(
                f"El usuario con {user.age} años es menor de edad")
        return func(user, *args, **kwargs)

    return wrapped


@is_adult
def comprar_licor(user):
    return f"El usuario con {user.age} años puede realizar la compra."


user1 = User(2006)

print(comprar_licor(user1))
