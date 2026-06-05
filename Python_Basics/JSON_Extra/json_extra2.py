import json


def read_pokemons_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        pokemons_list = json.load(file)
        return pokemons_list


def filter_pokemon_by_type(pokemons_list):
    user_type = input(
        "Ingrese el tipo de pokemon desea buscar: ")
    print("Los pokemos que existen de ese tipo son: ")

    found_match = False

    for pokemon in pokemons_list:
        if pokemon['type'].lower() == user_type.lower():
            print(pokemon['name'])

            found_match = True

    if not found_match:
        print(f"No existen pokemons del tipo '{user_type}'")


def main():
    file_path = "../General/pokemons.json"

    pokemons_list = read_pokemons_json(file_path)

    filter_pokemon_by_type(pokemons_list)


main()
