import random

random_number = random.randint(1, 10)

number_user = int(input("Guess the random number generated: "))

while number_user != random_number:
    print("Not the right one!")
    number_user = int(input("Try one more time "))
print("You got it right!")
