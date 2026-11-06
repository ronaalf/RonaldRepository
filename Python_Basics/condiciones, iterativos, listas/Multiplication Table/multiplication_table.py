number = int(input("Enter a number between 1 to 10: "))

inc_number = 0
result = 0

if number <= 10:
    for inc_number in range(1, 13):
        result = number * inc_number
        print(f"{number} * {inc_number} = {result}")

        