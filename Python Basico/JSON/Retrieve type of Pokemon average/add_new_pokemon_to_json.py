import json
from collections import defaultdict


def group_by_type(path_list):
    try:
        with open(path_list, 'r', encoding='utf-8') as f:
            pokemons = json.load(f)
    except FileNotFoundError:
            print("File does not exist")
    except json.JSONDecodeError:
            print("File is damaged")
            return

    groups = defaultdict(list)

    for pokemon in pokemons:
        groups[pokemon['type']].append(pokemon['level'])

    for type_name, levels in groups.items():
        average = sum(levels) / len(levels)
        print(f"Type: {type_name} → Level Average: {average}")


group_by_type('pokemon_list.json')