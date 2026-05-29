students_list = []


def register_student(students_list):
    new_student = {}

    new_student['full_name'] = input("Nombre del estudiante: ")
    new_student['section'] = input("Sección: ")

    new_student["spanish_grade"] = request_valid_grade("español")
    new_student['english_grade'] = request_valid_grade("inglés")
    new_student['history_grade'] = request_valid_grade("sociales")
    new_student['science_grade'] = request_valid_grade("ciencias")

    students_list.append(new_student)

    print("\n¡Estudiante registrado con éxito!")

    return students_list


def request_valid_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Digite la nota de {subject_name}: "))
            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Digite una nota valida (0 a 100)")
        except ValueError as ex:
            print(
                f"Error: Debes ingresar un número válido (sin letras ni espacios). Detalles: {ex}\n")
