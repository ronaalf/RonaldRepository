def songs_function(path):
    with open(path, 'r', encoding='utf') as file:
        content = file.readlines()
        sort_songs = sorted(content)
    with open('sorted_songs.txt', 'x', encoding='utf') as file:
        file.writelines(sort_songs)

songs_function('songs.txt')