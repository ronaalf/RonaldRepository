import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for games in reader:
            print(f"Name: {games['Name']}\nGenre: {games['Genre']}\nDeveloper: {games['Developer']}\nScore: {games['Score']}\n-----")

read_games('video_games_info.csv')