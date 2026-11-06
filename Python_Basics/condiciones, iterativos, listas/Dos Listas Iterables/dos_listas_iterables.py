first_list = ['There', 'cases', 'index', 'is', 'useful',]
second_list = ['are', 'where', 'iteration', 'very', "."]
"""
for first, second in zip(first_list, second_list):
    print(f"{first} {second}")
"""
for length in range(len(first_list)):
    print(f"{first_list[length]} {second_list[length]}")