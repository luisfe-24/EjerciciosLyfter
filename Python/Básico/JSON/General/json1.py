import json


def read_pokemons(file_path):
    with open(file_path, "r", encoding='utf-8') as file:

        pokemons_list = json.load(file)
        return pokemons_list


def get_new_pokemon():
    pokemon_name = input("Ingresa el nombre del pokemon: ")
    pokemon_type = input("Ingresa el tipo del pokemon: ")

    new_pokemon = {"name": pokemon_name, "type": pokemon_type}

    return new_pokemon


def save_pokemons(file_path, pokemons_list):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(pokemons_list, file, indent=4)


def main():
    file_path = "../General/pokemons.json"

    current_pokemons = read_pokemons(file_path)

    new_pokemon = get_new_pokemon()

    current_pokemons.append(new_pokemon)

    save_pokemons(file_path, current_pokemons)


main()
