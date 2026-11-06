my_list = ["10", "apple", "5.5", "3", "n/a"]

def sum_values(my_list):
    adding_value = []
    for element in my_list:
        try:
            float_value = float(element)
            if float_value:
                adding_value.append(float_value)
                print(f"{float_value} \"adding correctly\"")
        except ValueError as ex:
            print(f"\"Invalid element: {element}\"")


    print(f"\"The total sum:\" {sum(adding_value)}")

sum_values(my_list)