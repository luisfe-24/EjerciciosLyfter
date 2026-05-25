def search_char(my_string, user_char):
    counter = 0

    for char in my_string:
        if user_char == char:
            counter += 1

    return counter


my_string = "programacion"
user_char = input("Ingrese el carácter que desea buscar: ")

counter = search_char(my_string, user_char)

print(f"Se ha encontrado {counter} veces el carácter")
