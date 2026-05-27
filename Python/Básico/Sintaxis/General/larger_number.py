number = 0

larger_number = 0

counter = 1

for counter in range(1, 4):
    number = int(input(f"Ingrese el numero {counter}: "))

    if larger_number < number:
        larger_number = number

print(f"El numero mayor es: {larger_number}")
