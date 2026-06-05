import csv


def read_videogames_genre(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)

        genres_count = {}
        for row in reader:
            genre = row["genre"]

            if genre not in genres_count:
                genres_count[genre] = 1
            else:
                genres_count[genre] += 1

        print("Géneros encontrados: ")

        for genre in sorted(genres_count):
            print(f"{genre}: {genres_count[genre]}")


def main():
    content = "../General/videojuegos.csv"

    read_videogames_genre(content)


main()
