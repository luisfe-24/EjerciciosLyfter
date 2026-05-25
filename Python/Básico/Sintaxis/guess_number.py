import random

secret_number = random.randint(1, 10)
user_guess = 0

while user_guess != secret_number:
    user_guess = int(input("Adivina el numero secreto: "))
    if user_guess != secret_number:
        print("No adivinaste, intenta otra vez.")

print("¡Advinaste!")
