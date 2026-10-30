counter = 1
numbers = []

while counter <= 3:
    number = int(input("Enter number"))
    numbers.append(number)
    counter = counter + 1
print(max(numbers))

