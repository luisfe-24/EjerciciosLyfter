user_list = []

total_numbers = int(input("Cantidad de numeros a ingresar: "))
total_number = 0

for index in range(total_numbers):
    number = int(input(f"Ingresa el numero {index + 1}: "))
    user_list.append(number)

target_number = int(input("El numero a buscar es: "))

for record in user_list:
    if record == target_number:
        total_number += 1

print(f"El numero {target_number} aparece {total_number} veces.")
