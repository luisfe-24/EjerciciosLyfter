def sum_values(my_list):
    total_sum = 0

    for value in my_list:
        try:
            convert_number = float(value)
            print(f"{convert_number} sumado correctamente")
            total_sum += convert_number
        except ValueError:
            print(f"Elemento inválido: {value}")
    print(f"Total de la suma: {total_sum}")


my_list = ['10', 'manzana', '5.5', '3', 'n/a']

sum_values(my_list)
