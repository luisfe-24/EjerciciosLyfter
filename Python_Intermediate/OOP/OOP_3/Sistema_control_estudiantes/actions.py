class Student:
    def __init__(self, full_name, section, spanish_grade=0, english_grade=0, history_grade=0, science_grade=0, average=0):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.history_grade = history_grade
        self.science_grade = science_grade
        self.average = average

    def calculate_average(self):
        self.average = (self.spanish_grade + self.english_grade +
                        self.history_grade + self.science_grade) / 4
        return self.average

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "history_grade": self.history_grade,
            "science_grade": self.science_grade,
            "average": self.average
        }


def student_exists(students_list, name, section):
    for student in students_list:
        if student.full_name == name and student.section == section:
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
    while True:
        full_name = input("Nombre del estudiante: ")
        if is_valid_name(full_name):
            break
        print("El nombre no puede estar vacío ni contener números.\n")

    while True:
        section = input("Sección: ")
        if is_valid_section(section):
            break
        print("Formato de sección inválido.\n")

    if student_exists(students_list, full_name, section):
        print("Este estudiante ya se encuentra registrado.")
        return students_list

    spanish_grade = request_valid_grade("español")
    english_grade = request_valid_grade("inglés")
    history_grade = request_valid_grade("sociales")
    science_grade = request_valid_grade("ciencias")

    new_student = Student(
        full_name=full_name,
        section=section,
        spanish_grade=spanish_grade,
        english_grade=english_grade,
        history_grade=history_grade,
        science_grade=science_grade
    )

    new_student.calculate_average()

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
            if student.full_name == name and student.section == section:
                students_list.remove(student)
                print("¡Estudiante eliminado con éxito!")
                return
    else:
        print("Operación cancelada. El estudiante no fue eliminado.")


def request_valid_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Digite la nota de {subject_name}: "))
            if 0 <= grade <= 100:
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
            print(f"Nombre: {student.full_name}")
            print(f"Sección : {student.section}")
            print(f"Nota de español: {student.spanish_grade}")
            print(f"Nota de inglés: {student.english_grade}")
            print(f"Nota de sociales: {student.history_grade}")
            print(f"Nota de ciencias: {student.science_grade}")
            print("\n")


def display_failed_students(students_list):
    if len(students_list) == 0:
        print("No hay estudiantes registrados aún.")
        return

    has_failed_students = False

    for student in students_list:
        failed_grades = []

        if student.spanish_grade < 60:
            failed_grades.append(
                f"Español: {student.spanish_grade}"
            )

        if student.english_grade < 60:
            failed_grades.append(
                f"Inglés: {student.english_grade}"
            )

        if student.history_grade < 60:
            failed_grades.append(
                f"Sociales: {student.history_grade}"
            )

        if student.science_grade < 60:
            failed_grades.append(
                f"Ciencias: {student.science_grade}"
            )

        if len(failed_grades) > 0:
            has_failed_students = True
            print(f"\nNombre: {student.full_name}")
            print(f"Sección: {student.section}")
            print("Materias reprobadas:")
            for subject in failed_grades:
                print(f"{subject}")

    if not has_failed_students:
        print("\nNo hay estudiantes reprobados en el sistema.")


def display_top_3(students_list):
    if len(students_list) == 0:
        print("No hay estudiantes registrados aún.\n")
        return

    top_3_list = sorted(
        students_list, key=lambda x: x.average, reverse=True)[:3]

    for i, student in enumerate(top_3_list, 1):
        print(
            f"{i}. {student.full_name} (Sección {student.section}) - Promedio: {student.average}")


def display_general_average(students_list):
    try:
        sum_average = 0
        for student in students_list:
            sum_average += student.average

        total_average = sum_average / len(students_list)
        print(f"El promedio general es: {total_average}")
    except ZeroDivisionError:
        print(f"Intentaste dividir 0 entre 0.")
