import csv


def read_videogames_by_developer(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)

        user_developer = input("Ingrese el desarrollador: ")

        search_results = []

        for row in reader:
            if row['developer'].lower() == user_developer.lower():
                game_details = f"- {row['name']} (Clasificación: {row['classification']}, Género: {row['genre']})"
                search_results.append(game_details)

        if search_results:
            print(f"Videojuegos desarrollados por {user_developer}:")
            for game in search_results:
                print(game)
        else:
            print(
                f"No se encontraron videojuegos del desarrollador: '{user_developer}'")


def main():
    content = "../General/videojuegos.csv"

    read_videogames_by_developer(content)


main()
