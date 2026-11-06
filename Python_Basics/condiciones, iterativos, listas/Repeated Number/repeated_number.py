counter = 1
list = []

while counter <= 5:
    number = int(input("Enter number: "))
    list.append(number)
    counter = counter + 1

search_number = int(input("Enter number to search: "))

if search_number in list:
    result = list.count(search_number)
    print(f"The number {search_number} repeats itself {result} times")
else:
    print(f"The number {search_number} is not on the list")
