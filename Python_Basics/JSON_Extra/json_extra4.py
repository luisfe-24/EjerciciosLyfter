import json


def read_pokemons_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        pokemons_list = json.load(file)
        return pokemons_list


def display_average_pokemon_type_level(pokemons_list):
    type_levels_sum = {}
    type_counts = {}

    for pokemon in pokemons_list:
        pokemon_type = pokemon['type']
        pokemon_level = pokemon['level']

        if pokemon_type not in type_counts:
            type_counts[pokemon_type] = 1
            type_levels_sum[pokemon_type] = pokemon_level
        else:
            type_counts[pokemon_type] += 1
            type_levels_sum[pokemon_type] += pokemon_level

    for pokemon_type in type_levels_sum:

        total_sum = type_levels_sum[pokemon_type]

        total_count = type_counts[pokemon_type]

        average = total_sum / total_count

        print(f"Tipo: {pokemon_type} → Promedio de nivel: {average}")


def main():
    file_path = "../General/pokemons.json"

    pokemons_list = read_pokemons_json(file_path)

    display_average_pokemon_type_level(pokemons_list)


main()
