def name_and_age():
    x = 10
    while x == 10:
        try:
            y = input()
            z = float(y)
        except (ValueError) as err:
            print("So your name is "+y+". That's a good name. Now enter your age in years.")
            break
        else:
            print("That's a number, not a name. Type in your name.")
            continue
    while x == 10:
        try:
            a = input()
            b = int(float(a))
        except (ValueError) as err:
            print("That's not a number. Type your age in as a number.")
            continue
        else:
            if b < 100:
                print("Ah, so you're "+str(b)+" years old. That means you'll be 100 in "+str(100-b)+" years.")
                break
            else:
                print("Oh wow, you're already at least 100!")
                break
name_and_age()
