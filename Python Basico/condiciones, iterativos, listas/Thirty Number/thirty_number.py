counter = 1
numbers = []

while counter <= 3:
    number = int(input("Enter a number: "))
    numbers.append(number)
    counter = counter + 1

total = sum(numbers)

if 30 in numbers or total == 30:
    print("you got this!")
else:
    print("Incorrect!")




