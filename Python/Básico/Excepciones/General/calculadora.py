def addition(actual_number, new_number):
    actual_number = actual_number + new_number
    return actual_number


def subtraction(actual_number, new_number):
    actual_number = actual_number - new_number
    return actual_number


def multiplication(actual_number, new_number):
    actual_number = actual_number * new_number
    return actual_number


def division(actual_number, new_number):
    try:
        return actual_number / new_number
    except ZeroDivisionError as ex:
        print(
            f"Error [ZeroDivisionError] No puedes dividir {actual_number} por 0. Detalles: {ex}")
        return actual_number


def delete_result(actual_number):
    actual_number = 0
    print(actual_number)
    return actual_number


def menu():
    try:
        operations = {
            1: "Suma",
            2: "Resta",
            3: "Multiplicación",
            4: "División",
            5: "Borrar resultado",
            6: "Salir"
        }
        actual_number = 0

        while True:
            for index, operation in operations.items():
                print(f"{index}. {operation}")
            print(f"Numero actual: {actual_number}")

            try:
                option_selected = int(input("Elija una opcion: "))

                if 1 <= option_selected <= 4:
                    new_number = float(input("Elija el numero a operar: "))
                    if option_selected == 1:
                        actual_number = addition(actual_number, new_number)
                    elif option_selected == 2:
                        actual_number = subtraction(actual_number, new_number)
                    elif option_selected == 3:
                        actual_number = multiplication(
                            actual_number, new_number)
                    elif option_selected == 4:
                        actual_number = division(actual_number, new_number)
                elif option_selected == 5:
                    actual_number = delete_result(actual_number)
                elif option_selected == 6:
                    break
                else:
                    print("Error: La opción seleccionada no existe.")
            except ValueError as ex:
                print(
                    f"Error [ValueError]: No se puede usar letras. Detalles: {ex}")
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado: {ex}")


menu()
