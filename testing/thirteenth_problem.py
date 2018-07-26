import math
def fibonacci_generator_formulaic():
    while 1 == 1:
        try:
            range_list = list(range(1,int(input("How many fibonacci numbers would you like to create?"))+1))
        except (ValueError) as err:
            print("That's not an integer. Type in an integer as a response.")
        else:
            break
    for element in range_list:
        fibonacci_number = (((1.6180339**element)-(-0.6180339**element))/2.236067977)
        print(round(fibonacci_number))
fibonacci_generator_formulaic()

def fibonacci_generator_essential():
    x = 0
    y = 1
    while 1 == 1:
        try:
            range_list = list(range(int(input("How many fibonacci numbers would you like to create?"))-1))
        except (ValueError) as err:
            print("That's not an integer. Type in an integer as a response.")
        else:
            break
    print(1)
    for element in range_list:
        z = x + y
        print(z)
        x = y
        y = z
fibonacci_generator_essential()
