new_text = input("Enter a random phrase: ")

def create_nonexistent_file(path, text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(text + "\n")

create_nonexistent_file('document.txt', new_text)