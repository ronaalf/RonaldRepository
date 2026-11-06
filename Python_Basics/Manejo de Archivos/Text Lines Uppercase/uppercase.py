def convert_uppercase(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        upper_content = content.upper()
        print(upper_content)



convert_uppercase('document.txt')