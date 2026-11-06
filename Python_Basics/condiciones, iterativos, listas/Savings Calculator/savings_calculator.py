print("---- Savings Calculator ----")

name = input("Enter your name: ")
monthly_savings = int(input("How many dollars do you save per month? "))
months = int(input("How many months do you wish to calculate? "))
total = 0

for month in range(1, months + 1):
    total = total + monthly_savings
    print(f"Month {month}: accumulated total = {total}")
print(f"{name}, in {months} months you will save {total}")