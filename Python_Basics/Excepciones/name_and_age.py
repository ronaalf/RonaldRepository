def name_user():
    try:
        name = input("Enter your name: ")
        
        for letter in name:
            if letter.isdigit():
                raise ValueError("Name cannot be a digit")    
        return name
    except ValueError as ex:
        print(f"Value entered is not a string. {ex}")


def age_user(name):
    try:
        age = input("Enter your age: ")
        
        for digit in age:
            if digit.isalpha():
                raise ValueError("Number not valid")
            
        print(f"Hello {name}, you are {age} years old!")

    except ValueError as ex:
        print(f"Value entered is not a digit. {ex}")


def main():
    try:
        op = name_user()
        age_user(op)

    except Exception as ex:
        print(f"Unknown error {ex}")


main()