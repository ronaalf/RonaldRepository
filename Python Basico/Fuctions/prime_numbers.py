list_numbers = [1, 4, 6, 7, 13, 9, 67]
prime_numbers_filtered = []


def prime_math_filter(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    prime_numbers_filtered.append(number)


def is_prime_number():
    global list_numbers
    for number in list_numbers:
        prime_math_filter(number)


is_prime_number()
print(prime_numbers_filtered)
