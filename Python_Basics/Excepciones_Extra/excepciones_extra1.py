def get_name():
    try:
        name = input("Ingrese su nombre: ")
        if name.isdigit():
            raise ValueError("El nombre no puede ser un numero")
        return name
    except ValueError as ex:
        print(ex)
        return None


def get_age():
    try:
        age = int(input("Ingrese su edad: "))
        return age
    except ValueError:
        print("Numero no valido")
        return None


def main():
    name = get_name()
    if name is None:
        return

    age = get_age()
    if age is None:
        return

    print(f"Hola {name}, su edad es {age}")


main()
