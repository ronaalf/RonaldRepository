import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for games in reader:
                score = float(games['Score'])
                if score == 9.4:
                    print(games)

read_games('video_games_info.csv')