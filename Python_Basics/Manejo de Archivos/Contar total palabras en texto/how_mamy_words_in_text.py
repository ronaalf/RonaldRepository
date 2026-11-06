def how_many_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        clean_words = content.split()
        total_words = len(clean_words)
        print(f"This file contains {total_words} words.")


how_many_words('words_as_a_text.txt')