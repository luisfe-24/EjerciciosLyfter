def student_exists(students_list, name, section):
    for student in students_list:
        if student["full_name"] == name and student["section"] == section:
            return True
    return False


def is_valid_name(name):
    if name.strip() == "":
        return False
    for char in name:
        if char.isdigit():
            return False
    return True


def is_valid_section(section):
    clean_section = section.strip()

    if len(clean_section) < 2 or len(clean_section) > 3:
        return False

    if not clean_section[:-1].isdigit():
        return False

    if not clean_section[-1].isalpha():
        return False

    return True


def register_student(students_list):
    new_student = {}

    while True:
        new_student["full_name"] = input("Nombre del estudiante: ")
        if is_valid_name(new_student["full_name"]):
            break
        print("El nombre no puede estar vacío ni contener números.\n")

    while True:
        new_student["section"] = input("Sección: ")
        if is_valid_section(new_student["section"]):
            break
        print("Formato de sección inválido.\n")

    if student_exists(
        students_list, new_student["full_name"], new_student["section"]
    ):
        print("Este estudiante ya se encuentra registrado.")
        return students_list

    new_student["spanish_grade"] = request_valid_grade("español")
    new_student["english_grade"] = request_valid_grade("inglés")
    new_student["history_grade"] = request_valid_grade("sociales")
    new_student["science_grade"] = request_valid_grade("ciencias")

    new_student["average"] = (
        new_student["spanish_grade"]
        + new_student["english_grade"]
        + new_student["history_grade"]
        + new_student["science_grade"]
    ) / 4

    students_list.append(new_student)

    print("\n¡Estudiante registrado con éxito!")

    return students_list


def delete_student(students_list, name, section):
    if not student_exists(students_list, name, section):
        print("\nEl estudiante no existe en el sistema.")
        return

    confirm = input(
        f"\n¿Está seguro de que desea eliminar a {name} de la sección {section}? (s/n): "
    )

    if confirm.lower() == "s":
        for student in students_list:
            if student["full_name"] == name and student["section"] == section:
                students_list.remove(student)
                print("¡Estudiante eliminado con éxito!")
                return
    else:
        print("Operación cancelada. El estudiante no fue eliminado.")


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


def display_all_students(students_list):
    if len(students_list) == 0:
        print("No hay estudiantes registrados aún.\n")
    else:
        for student in students_list:
            print(f"Nombre: {student['full_name']}")
            print(f"Sección : {student['section']}")
            print(f"Nota de español: {student['spanish_grade']}")
            print(f"Nota de inglés: {student['english_grade']}")
            print(f"Nota de sociales: {student['history_grade']}")
            print(f"Nota de ciencias: {student['science_grade']}")
            print("\n")


def display_failed_students(students_list):
    if len(students_list) == 0:
        print("No hay estudiantes registrados aún.")
        return

    hay_reprobados = False

    for student in students_list:
        failed_grades = []

        if student["spanish_grade"] < 60:
            failed_grades.append(
                f"Español: {student['spanish_grade']}"
            )

        if student["english_grade"] < 60:
            failed_grades.append(
                f"Inglés: {student['english_grade']}"
            )

        if student["history_grade"] < 60:
            failed_grades.append(
                f"Sociales: {student['history_grade']}"
            )

        if student["science_grade"] < 60:
            failed_grades.append(
                f"Ciencias: {student['science_grade']}"
            )

        if len(failed_grades) > 0:
            hay_reprobados = True
            print(f"\nNombre: {student['full_name']}")
            print(f"Sección: {student['section']}")
            print("Materias reprobadas:")
            for materia in failed_grades:
                print(f"{materia}")

    if not hay_reprobados:
        print("\nNo hay estudiantes reprobados en el sistema.")


def display_top_3(students_list):
    if len(students_list) == 0:
        print("No hay estudiantes registrados aún.\n")
        return

    top_3_list = []

    for student in students_list:
        if len(top_3_list) == 0 or student["average"] > top_3_list[0]["average"]:
            top_3_list.insert(0, student)

        elif (
            len(top_3_list) == 1
            or student["average"] > top_3_list[1]["average"]
        ):
            top_3_list.insert(1, student)

        elif (
            len(top_3_list) == 2
            or student["average"] > top_3_list[2]["average"]
        ):
            top_3_list.insert(2, student)

        if len(top_3_list) > 3:
            top_3_list.pop()

    for student in top_3_list:
        print(f"{student['full_name']}: {student['average']}")


def display_general_average(students_list):
    try:
        sum_average = 0
        for student in students_list:
            sum_average += student['average']

        total_average = sum_average / len(students_list)
        print(total_average)
    except ZeroDivisionError:
        print(f"Intentaste dividir 0 entre 0.")
