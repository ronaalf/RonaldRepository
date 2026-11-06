def vocals_in_text():
    string_text = "hello world"

    counter = 0

    vocals = "aeiouAEIOU"

    for letter in string_text:
        if letter in vocals:
            letter_length = len(letter)
            counter = counter + 1

    print(counter)


vocals_in_text()