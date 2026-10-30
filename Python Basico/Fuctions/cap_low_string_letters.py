def string_sensitive():
    string_itself = "I love Houses Sushi"

    upper = 0
    lower = 0

    for letter in string_itself:
        if letter.islower():
            lower = lower + 1
        elif letter.isupper():
            upper = upper + 1

    print(f"There are {upper} upper cases and {lower} lower cases")

string_sensitive()