import csv


def export_students_data(file_path, data):
    if len(data) == 0:
        print("No hay datos para exportar.")
        return

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(data)

    print("¡Archivo exportado con éxito!")


def import_students_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            loaded_students = []
            for student in reader:
                student["spanish_grade"] = float(student["spanish_grade"])
                student["english_grade"] = float(student["english_grade"])
                student["history_grade"] = float(student["history_grade"])
                student["science_grade"] = float(student["science_grade"])
                student["average"] = float(student["average"])

                loaded_students.append(student)
            print("¡Datos importados con éxito!")
            return loaded_students

    except FileNotFoundError:
        print("No hay un archivo previamente exportado. Registra y exporta datos primero.")
        return []
