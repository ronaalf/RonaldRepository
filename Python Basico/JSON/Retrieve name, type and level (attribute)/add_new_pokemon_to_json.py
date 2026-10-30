import json

def read_and_add_pokemon(path_list):
    try:
        with open(path_list, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for pokemon in data:
                print(f"Name: {pokemon['name']}.\nType: {pokemon['type']}.\nLevel: {pokemon['level']}.\n-----")
    except FileNotFoundError:
            print("File does not exist")
    except json.JSONDecodeError:
            print("File is damaged")
            return


read_and_add_pokemon('pokemon_list.json')