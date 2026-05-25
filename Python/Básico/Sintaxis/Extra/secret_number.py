import random

secret_number = random.randint(1, 10)

user_number = 0

while user_number != secret_number:
    print("Adivina el numero secreto: ")
    user_number = int(input())

    if user_number != secret_number:
        print("No adivinaste, intenta de nuevo: ")

print("¡Adivinaste!")
