from actions import Student
import csv


def export_students_data(file_path, data):
    if len(data) == 0:
        print("No hay datos para exportar.")
        return

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        dict_data = [student.to_dict() for student in data]

        headers = dict_data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(dict_data)

    print("¡Archivo exportado con éxito!")


def import_students_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            loaded_students = []

            for row in reader:
                # 🌟 Convertimos el diccionario que lee csv.DictReader a un OBJETO Student
                student_obj = Student(
                    full_name=row["full_name"],
                    section=row["section"],
                    spanish_grade=float(row["spanish_grade"]),
                    english_grade=float(row["english_grade"]),
                    history_grade=float(row["history_grade"]),
                    science_grade=float(row["science_grade"]),
                    average=float(row["average"])
                )

                loaded_students.append(student_obj)

            print("¡Datos importados con éxito!")
            return loaded_students

    except FileNotFoundError:
        print("No hay un archivo previamente exportado. Registra y exporta datos primero.")
        return []
