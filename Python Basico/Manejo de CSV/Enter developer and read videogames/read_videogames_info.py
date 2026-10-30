import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        developer = input("Enter the developer's name: ")

        print(f"Video games developed by {developer}: ")
        
        for games in reader:
            by_developer = games['Developer']
            if developer in by_developer:
                print(f"- {games['Name']} (Score: {games['Score']}, Genre: {games['Genre']})")

read_games('video_games_info.csv')