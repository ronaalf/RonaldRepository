def alp_words():
    words = "python-variable-function-computer-monitor"

    # right_text = "-".join(sorted(words.split("-")))

    list_words = words.split("-")
    sorted_list = sorted(list_words)
    sorted_string = "-".join(sorted_list)
    print(sorted_string)


alp_words()
