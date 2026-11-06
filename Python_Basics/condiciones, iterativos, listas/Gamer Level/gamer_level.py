print("---- Gamer-Level Sorter ----")

name = input("Enter your name: ")
hours = int(input("How many hours have you been playing?"))
is_competitive = input("Do you play competitively? (yes/no): ")

if hours < 10:
    category = "Junior"
    message = "Welcome to the gaming world"
elif hours < 50:
    category = "Casual"
    message = "You're getting on track!"
elif hours < 200:
    category = "Gamer"
    message = "Definitely, you know what you're doing."
elif hours >= 200 and is_competitive == "yes":
    category = "Pro"
    message = "You are a living legend."
else:
    category = "Gamer"
    message = "You have the experience, but you haven't entered the competitive scene yet."

print (f"{name} your category level is: {category}")
print(message)