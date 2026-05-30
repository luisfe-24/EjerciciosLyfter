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


def import_students_data():
    print("hello")
