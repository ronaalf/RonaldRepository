import json

def ask_int(message, minimum=None):
    while True:
        try:
            value = int(input(message))
            if minimum is not None and value < minimum:
                print(f"Value must be higher or equal than {minimum}.")
                continue
            return value
        except ValueError:
            print("An integer value must be entered.")


def ask_float(message, minimum=None):
    while True:
        try:
            value = float(input(message))
            if minimum is not None and value < minimum:
                print(f"Value must be higher or equal than {minimum}.")
                continue
            return value
        except ValueError:
            print("A number must be entered.")


def ask_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This input is required")


def ask_bool(message):
    while True:
        value = input(message).strip().lower()
        if value in ("y", "s", "si", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Enter (y/n).")

def read_and_add_pokemon(path_list):
    try:
        with open(path_list, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
            print("File does not exist")
    except json.JSONDecodeError:
            print("File is damaged")
            return
    
    if isinstance(data, dict):
                data = [data]

    skills_input = ask_text("Skills (Separated by commas): ")
    skills = [s.strip() for s in skills_input.split(",")if s.strip()]

    new_pokemon = {
        "name": ask_text("Name: "),
        "type": ask_text("Type: "),
        "level": ask_int("Level: ", minimum=1),
        "weight_kg": ask_float("Weight (kg): ", minimum=0),
        "is_shiny": ask_bool("Is shiny (y/n): "),
        "held_item": input("Held item (Enter for none): ").strip() or None,
        "skills": skills,
        "stats": {
            "hp": ask_int("HP: ", minimum=0),
            "attack": ask_int("Attack: ", minimum=0),
            "defense": ask_int("Defense: ", minimum=0),
            "sp_attack": ask_int("Sp_attack: ", minimum=0),
            "sp_defense": ask_int("Sp.defense: ", minimum=0),
            "speed": ask_int("Speed: ", minimum=0),
            },
    }

    data.append(new_pokemon)

    try:
        with open(path_list, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            print("Data saved successfully!")
    except OSError as e:
        print(f"File was not saved. {e}")


read_and_add_pokemon('pokemon_list.json')