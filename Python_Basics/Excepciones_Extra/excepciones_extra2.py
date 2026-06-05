def convert_to_integer(my_list):
    print("Resultado:")

    for value in my_list:
        try:
            convert_number = int(value)
            print(f"'{value}' convertido a {convert_number}")
        except ValueError:
            print(f"No se pudo convertir el elemento: {value}")


my_list = ['4', 'hola', '10', '5.2']


convert_to_integer(my_list)
