list = ["4", "hola", "10", "5.2"]



def convert_to_integer(list):
    print("\"Result:\"")
    for value in list:
        try:
            int_value = int(value)
            print(f"\"{value}\" \"converted to\" {int_value}")
            
        except ValueError as ex:
            print(f"\"It cannot be converted: {value}\"")


convert_to_integer(list)
