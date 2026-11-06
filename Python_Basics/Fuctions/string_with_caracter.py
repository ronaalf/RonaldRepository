def character_filter():
    string = "programming"
    user_character = input("Enter the character you wish to locate into string: ")

    counter = 0

    for letter in string:
        if letter == user_character:
            counter = counter + 1 
    print(f"String contains {counter} times the character")


character_filter()