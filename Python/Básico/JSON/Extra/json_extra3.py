import json


def read_pokemons_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        pokemons_list = json.load(file)
        return pokemons_list


def display_pokemon_stats(pokemons_list):
    for pokemon in pokemons_list:
        print(f"Nombre: {pokemon['name']}")
        pokemon_stats = pokemon['stats']
        print(f"HP: {pokemon_stats['hp']}")
        print(f"Ataque: {pokemon_stats['attack']}")
        print(f"Defensa: {pokemon_stats['defense']}")
        print(f"Ataque Esp.: {pokemon_stats['sp_attack']}")
        print(f"Defensa Esp.: {pokemon_stats['sp_defense']}")
        print(f"Velocidad: {pokemon_stats['speed']}")
        print("")


def main():
    file_path = "../General/pokemons.json"

    pokemons_list = read_pokemons_json(file_path)

    display_pokemon_stats(pokemons_list)


main()
