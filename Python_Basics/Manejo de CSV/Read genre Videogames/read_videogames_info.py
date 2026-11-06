import csv

def read_games(file_path):
    counter = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for games in reader:
                genre = games['Genre']
                if genre in counter:
                    counter[genre] += 1
                else:
                    counter[genre] = 1

    print("Genre found:")
    
    for genre in sorted(counter.keys()):
        print(f"{genre}: {counter[genre]}")

read_games('video_games_info.csv')