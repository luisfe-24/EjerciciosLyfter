user_number = int(input("Ingrese un número del 1 al 10: "))

for counter in range(1, 13):
    multiplication_result = user_number * counter
    print(f"{user_number} x {counter} = {multiplication_result}")
