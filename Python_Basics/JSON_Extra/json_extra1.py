import json


def read_pokemons_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        pokemons_list = json.load(file)
        return pokemons_list


def display_pokemon_details(pokemons_list):
    print("Info de Pokemons")
    for pokemon in pokemons_list:
        print(f"Nombre: {pokemon['name']}")
        print(f"Tipo: {pokemon['type']}")
        print(f"Nivel: {pokemon['level']}")
        print(f"Peso: {pokemon['weight_kg']} kg")
        print(f"¿Es Shiny?: {'Sí' if pokemon['is_shiny'] else 'No'}")

        if pokemon['held_item'] is not None:
            print(f"Objeto equipado: {pokemon['held_item']}")
        else:
            print("Objeto equipado: Ninguno")

        print("Habilidades:")
        for skill in pokemon['skills']:
            print(f"  - {skill}")

        pokemon_stats = pokemon['stats']
        print("Estadísticas:")
        print(f"  - HP: {pokemon_stats['hp']}")
        print(f"  - Ataque: {pokemon_stats['attack']}")
        print(f"  - Defensa: {pokemon_stats['defense']}")
        print(f"  - Ataque Esp.: {pokemon_stats['sp_attack']}")
        print(f"  - Defensa Esp.: {pokemon_stats['sp_defense']}")
        print(f"  - Velocidad: {pokemon_stats['speed']}")
        print("")


def main():
    file_path = "../General/pokemons.json"

    pokemons_list = read_pokemons_json(file_path)

    display_pokemon_details(pokemons_list)


main()
