def choose_your_number():
    print("Okay. Write a number to find out if it's evenly divisible by 2, 4 or neither.")
    while 1 == 1:
        x = input()
        try:
            y = float(x)
        except (ValueError) as err:
            print("That's not a number. Type in a number.")
            continue
        else:
            if y%1 != 0:
                print(str(x)+" is a float, not an integer. Of course it's not evenly divisible by 2 or 4!")
                break
            else:
                if y%4 == 0:
                    print(str(int(x))+" is divisible by both 2 and 4!")
                    break
                elif y%2 == 0:
                    print(str(int(x))+" is divisible by 2, but not by 4.")
                    break
                else:
                    print(str(int(x))+" isn't divisible by either 2 or 4. Sorry.")
                    break

def choose_your_two_numbers():
    print("Okay. Write one number, hit enter, then write your second number and hit enter. Numerical characters only.")
    while 1 == 1:
        first_response = input()
        second_response = input()
        try:
            float(first_response)
            float(second_response)
            (float(first_response))/(float(second_response))
        except (ValueError) as err:
            print("Those aren't purely numerical characters. Try again.")
            continue
        except (ZeroDivisionError) as err:
            print("You can't divide by zero. Enter a different number for the divisor.")
            continue
        else:
            if float(first_response)%1 != 0 and float(second_response)%1 != 0:
                product1 = (float(first_response)/float(second_response))
                print("The product is "+str(product1)+".")
                break
            elif float(first_response)%1 != 0 and float(second_response)%1 == 0:
                product2 = (float(first_response)/float(second_response))
                print("The product is "+str(product2)+".")
                break
            elif float(first_response)%1 == 0 and float(second_response)%1 != 0:
                product3 = (float(first_response)/float(second_response))
                print("The product is "+str(product3)+".")
                break
            else:
                product4 = (int(first_response)/int(second_response))
                print("The product is "+str(product4)+".")
                break

def choose():
    print("Do you want to test one number, or two?")
    while 1 == 1:
        initial_response = input()
        try:
            int(float(initial_response))
        except (ValueError) as err:
            if initial_response.lower() == "one":
                choose_your_number()
                break
            elif initial_response.lower() == "two":
                choose_your_two_numbers()
                break
            else:
                print("That's not a valid answer to the question, try again by typing words or whole numbers.")
                continue
        else:
            if int(float(initial_response)) == 1:
                choose_your_number()
                break
            elif int(float(initial_response)) == 2:
                choose_your_two_numbers()
                break
            else:
                print("That's not a valid answer to the question, try again.")
                continue
choose()
