import csv

def save_video_games_info(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)


top_10_video_games = [
    {
        "Name": "The Legend of Zelda: Breath of the Wild",
        "Platform": "Nintendo Switch",
        "Score": 9.7,
        "Hours_to_Beat": 50,
        "Players": "Single-player",
        "Genre": "Action-Adventure",
        "Year": 2017,
        "Developer": "Nintendo EPD",
    },
    {
        "Name": "The Witcher 3: Wild Hunt",
        "Platform": "PC",
        "Score": 9.6,
        "Hours_to_Beat": 52,
        "Players": "Single-player",
        "Genre": "RPG",
        "Year": 2015,
        "Developer": "CD Projekt Red",
    },
    {
        "Name": "Red Dead Redemption 2",
        "Platform": "PlayStation 4",
        "Score": 9.5,
        "Hours_to_Beat": 48,
        "Players": "Single-player, Multiplayer",
        "Genre": "Action-Adventure",
        "Year": 2018,
        "Developer": "Rockstar Games",
    },
    {
        "Name": "God of War",
        "Platform": "PlayStation 4",
        "Score": 9.4,
        "Hours_to_Beat": 20,
        "Players": "Single-player",
        "Genre": "Action",
        "Year": 2018,
        "Developer": "Santa Monica Studio",
    },
    {
        "Name": "Elden Ring",
        "Platform": "PC",
        "Score": 9.4,
        "Hours_to_Beat": 60,
        "Players": "Single-player, Multiplayer",
        "Genre": "Action RPG",
        "Year": 2022,
        "Developer": "FromSoftware",
    },
    {
        "Name": "Hades",
        "Platform": "PC",
        "Score": 9.3,
        "Hours_to_Beat": 22,
        "Players": "Single-player",
        "Genre": "Roguelike",
        "Year": 2020,
        "Developer": "Supergiant Games",
    },
    {
        "Name": "Portal 2",
        "Platform": "PC",
        "Score": 9.2,
        "Hours_to_Beat": 9,
        "Players": "Single-player, Co-op",
        "Genre": "Puzzle",
        "Year": 2011,
        "Developer": "Valve",
    },
    {
        "Name": "Super Mario Odyssey",
        "Platform": "Nintendo Switch",
        "Score": 9.2,
        "Hours_to_Beat": 13,
        "Players": "Single-player, Co-op",
        "Genre": "Platformer",
        "Year": 2017,
        "Developer": "Nintendo EPD",
    },
    {
        "Name": "Hollow Knight",
        "Platform": "PC",
        "Score": 9.0,
        "Hours_to_Beat": 27,
        "Players": "Single-player",
        "Genre": "Metroidvania",
        "Year": 2017,
        "Developer": "Team Cherry",
    },
    {
        "Name": "Minecraft",
        "Platform": "Multi-platform",
        "Score": 9.0,
        "Hours_to_Beat": 100,
        "Players": "Single-player, Multiplayer",
        "Genre": "Sandbox",
        "Year": 2011,
        "Developer": "Mojang Studios",
    },
]


save_video_games_info('new_video_games_info.csv', top_10_video_games)