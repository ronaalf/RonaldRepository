def select_operator(math_options, current_number):        
    
    print(f"Your current number is {current_number}")

    for i, option in enumerate(math_options, start=1):
        print(f"{i}. {option}")
        
    try:
        user_option = int(input("Enter an option number of the list: ")) - 1
        operator_selected = math_options[user_option]
        print(operator_selected)
        return operator_selected
    except IndexError as ex: 
        print(f"Option is not valid. {ex}")
    except ValueError as ex:
            print(f"Not valid. {ex}")

def calculate_number(current_number, operator_selected):
    counter = 1
    
    while operator_selected and counter == 1:
        counter += counter + 1
        try:
            if operator_selected == "remove result":
                current_number = 0
                print(f"Result was removed successfully {current_number}")
                return
            
            user_number = int(input("Enter a number: "))
            
            if operator_selected == "sum":
                current_number += user_number
                print(current_number)
            elif operator_selected == "subtract":
                current_number -= user_number
                print(current_number)
            elif operator_selected == "multiply":
                current_number *= user_number
                print(current_number)
            elif operator_selected == "divide":
                current_number /= user_number
                print(current_number) 

        except ValueError as ex:
            print(f"Number invalid! {ex}")

        except ZeroDivisionError as ex:
            print(f"Cannot be divided by zero. {ex}")


def main():

    math_options = ["sum", "subtract", "multiply", "divide", "remove result"]
    current_number = 2

    try:
        op = select_operator(math_options, current_number)
        calculate_number(current_number, op)
    except Exception as ex:
        print(F"Unexpected error {ex}")


main()