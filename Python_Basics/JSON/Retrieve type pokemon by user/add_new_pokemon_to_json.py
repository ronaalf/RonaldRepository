import json

def read_and_add_pokemon(path_list):
    pokemon_type = input("Enter the Pokemon type: ")
    try:
        with open(path_list, 'r', encoding='utf-8') as f:
            data = json.load(f)

            print("Available Pokemon are: ")

            for pokemon in data:
                if pokemon_type in pokemon['type']:
                    print(f"- {pokemon['name']}")

    except FileNotFoundError:
            print("File does not exist")
    except json.JSONDecodeError:
            print("File is damaged")
            return


read_and_add_pokemon('pokemon_list.json')