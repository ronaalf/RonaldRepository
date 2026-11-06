first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))


if age < 4:
    age_group = "a baby/infant"
elif age < 11:
    age_group = "a child"
elif age < 14:
    age_group = "a pre-adolescent"
elif age < 19:
    age_group = "a teenager"
elif age < 29:
    age_group = "a young adult"
elif age < 64:
    age_group = "an adult"
else:
    age_group = "an elderly person/Senior"

print(f"Hello, {first_name} {last_name}! You are {age} years old. Therefore, you are {age_group}.")