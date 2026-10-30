my_list = [10, 20, 30, 40, 50]

total_numbers = len(my_list)
total = sum(my_list)
average = int(total / total_numbers)

print(f"The average is: {average}")

new_list = []

for list in my_list:
    if list > 30:
        new_list.append(list)

print(f"New list: {new_list}")