name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age < 6:
    print(f"{name}, eres un bebe")

elif age < 12:
    print(f"{name}, eres un niño")

elif age < 15:
    print(f"{name}, eres un preadolescente")

elif age < 20:
    print(f"{name}, eres un adolescente")

elif age < 25:
    print(f"{name}, eres un adulto joven")

elif age < 60:
    print(f"{name}, eres un adulto")

else:
    print(f"{name}, eres un adulto mayor")
