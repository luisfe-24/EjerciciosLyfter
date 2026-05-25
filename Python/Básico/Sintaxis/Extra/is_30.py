first_number = int(input("Ingrese el primer numero: "))
second_number = int(input("Ingrese el segundo numero: "))
third_number = int(input("Ingrese el tercer numero: "))

if first_number + second_number + third_number == 30:
    print("Correcto")

elif first_number == 30 or second_number == 30 or third_number == 30:
    print("Correcto")

else:
    print("Incorrecto")
