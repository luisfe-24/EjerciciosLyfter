
user_logged_in = False


def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError("Usuario no autenticado")
        else:
            return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile(name):
    print(f"Mostrando perfil del usuario {name}")


view_profile("Luis")
