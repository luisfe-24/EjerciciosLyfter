from actions import *
from data import *


def menu():
    print("Sistema de control de  estudiantes")
    print("1. Registrar estudiante")
    print("2. Ver todos los estudiantes")
    print("3. Ver top 3 estudiantes")
    print("4. Ver Promedio general")
    print("5. Exportar datos")
    print("6. Importar datos")
    print("7. Salir")

    while True:
        try:
            user_option = int(input("Elija una opcion del menu: "))

            if user_option == 1:
                register_student(students_list)
            elif user_option == 2:
                display_all_students(students_list)
            elif user_option == 3:
                display_top_3(students_list)
            elif user_option == 4:
                display_general_average(students_list)
            elif user_option == 5:
                export_students_data()
            elif user_option == 6:
                import_students_data()
            elif user_option == 7:
                break
            else:
                print("Seleccionaste un numero invalido.")

        except ValueError as ex:
            print(
                f"Tienes que elegir un numero entero valido. Detalles: {ex}")
