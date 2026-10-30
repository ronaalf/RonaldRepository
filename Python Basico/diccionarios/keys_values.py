list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer',]

user = {}

for list in range(len(list_a)):
    key = list_a[list]
    value = list_b[list]

    user[key] = value

print(user)

