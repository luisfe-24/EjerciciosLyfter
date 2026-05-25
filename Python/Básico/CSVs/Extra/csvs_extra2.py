import csv


def read_videogames_by_genre(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        reader = csv.reader(file)

        next(reader)

        user_classification = input("Ingrese la clasificación: ")
        for row in reader:
            if row[3] == user_classification.upper():
                print(f"Nombre: {row[0]}")
                print(f"Género: {row[1]}")
                print(f"Desarrollador: {row[2]}")
                print(f"Clasificación: {row[3]}")
                print("")


def main():
    content = "../General/videojuegos.csv"

    read_videogames_by_genre(content)


main()
