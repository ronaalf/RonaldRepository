def words_list():
    number_user = int(input("Enter number of letters: "))

    list_of_words = ["seven", "two", "wonderful", "sun"]
    words_returned = []

    for word in list_of_words:
        if len(word) >= number_user:
            words_returned.append(word)
    print(words_returned)


words_list()