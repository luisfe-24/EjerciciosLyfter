my_list = [3, 6, 0, -2, 4]

all_positive = True

for record in my_list:

    if record < 1:
        all_positive = False
        break

if all_positive:
    print("Todos los elementos de la lista son positivos")
else:
    print("Hay al menos un número negativo o cero")
