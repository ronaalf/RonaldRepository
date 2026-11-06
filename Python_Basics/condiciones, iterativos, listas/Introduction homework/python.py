first_number = 1
second_number = 90
third_number = 430
forth_number = 4

print(first_number + first_number)
print(second_number - third_number)
print(forth_number * 5)
print(50 / 10)

name = input("What's your name?")
age = int(input("How old are you?"))
favorite_color = input("What's your favorite color?")
favorite_dish = input("What's your favorite dish?")

print(f"My name is {name}!")
print(f"I'm {age} years old")
print(f"My favorite color is {favorite_color}")
print(f"My favorite dish is {favorite_dish}")


my_current_age = int(input("How old am I?"))
years = 10

future_age = my_current_age + years

print(f"In 10 years from now I'll be {future_age} years old")



meters = int(input("How many meters?"))

if meters:
    centimeters = meters * 100
    print(f"{meters} meters are {centimeters} centimeters.")