from actions import (display_all_students, display_general_average,
                     display_top_3, register_student, delete_student)
from data import (export_students_data, import_students_data)

students_list = []


def menu():
    global students_list

    print("Sistema de control de  estudiantes")
    print("1. Registrar estudiante")
    print("2. Eliminar estudiante")
    print("3. Ver todos los estudiantes")
    print("4. Ver top 3 estudiantes")
    print("5. Ver Promedio general")
    print("6. Exportar datos")
    print("7. Importar datos")
    print("8. Salir")

    while True:
        try:
            user_option = int(input("Elija una opcion del menu: "))

            if user_option == 1:
                register_student(students_list)
            elif user_option == 2:
                name_to_delete = input(
                    "Ingrese el nombre completo del estudiante a eliminar: ")
                section_to_delete = input("Ingrese la seccion (ej. 11B): ")

                delete_student(students_list, name_to_delete,
                               section_to_delete)
            elif user_option == 3:
                display_all_students(students_list)
            elif user_option == 4:
                display_top_3(students_list)
            elif user_option == 5:
                display_general_average(students_list)
            elif user_option == 6:
                export_students_data('students_list.csv', students_list)
            elif user_option == 7:
                students_list = import_students_data('students_list.csv')
            elif user_option == 8:
                break
            else:
                print("Seleccionaste un numero invalido.")

        except ValueError as ex:
            print(
                f"Tienes que elegir un numero entero valido. Detalles: {ex}")
