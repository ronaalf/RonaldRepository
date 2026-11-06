number = int(input("Enter a number: "))

counter = 1
total_sum = 0

while counter <= number:
    total_sum = total_sum + counter
    counter = counter + 1 
print(f"The total sum is {total_sum}")