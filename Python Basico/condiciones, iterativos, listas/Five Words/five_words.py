counter = 1
five_words = []
longer_words = []

while counter <= 5:
    counter = counter + 1
    five_words_user = input("Enter a random word: ")
    five_words.append(five_words_user)

for single_word in five_words:
    length_word = len(single_word)
    if length_word > 4:
        longer_words.append(single_word)

print(five_words)
print(longer_words)

