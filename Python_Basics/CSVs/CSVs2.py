import csv


def get_videogames():
    games_list = []

    while True:
        try:
            amount_games = int(
                input("¿Cuántos videojuegos deseas registrar?: "))
            if amount_games <= 0:
                print("Por favor, ingresa un número mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    for index in range(amount_games):
        name = input("Nombre: ")
        genre = input("Genero: ")
        developer = input("Desarrollador: ")
        classification = input("clasificacion: ")

        game = {
            "name": name,
            "genre": genre,
            "developer": developer,
            "classification": classification
        }
        games_list.append(game)

    return games_list


def save_games_list(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')

        writer.writeheader()

        writer.writerows(data)


def main():
    registered_videogames = get_videogames()

    save_games_list('videojuegos2.csv', registered_videogames)


main()
