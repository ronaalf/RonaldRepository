def read_complete_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            print(line.strip(), end= " ")

read_complete_file('hello_world.txt')