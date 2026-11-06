counter = 1
list = []

while counter <= 10:
    number = int(input("Enter a number: "))
    list.append(number)
    counter = counter + 1 
print(f"{list} The higher one was: {max(list)}")