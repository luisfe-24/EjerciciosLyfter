def min_length_list(my_list, user_number):
    new_list = []

    for word in my_list:
        if len(word) > user_number:
            new_list.append(word)

    return new_list


my_list = ["cielo", "sol", "maravilloso", "día"]

user_number = int(
    input(f"Ingrese el numero de letras minimas en la palabra: "))

print(min_length_list(my_list, user_number))
