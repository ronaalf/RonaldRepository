global_value = 1


def function_1():
    global global_value
    global_value = global_value + 1
    print(f"Global value 1 changed to {global_value}")
    interned_value = 5
    function_2(interned_value)


def function_2(interned_value):
    if interned_value == 5:
        print("Internal variable was successfully to another function")


function_1()
