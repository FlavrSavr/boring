def guessing_game():
    import random
    while 1 == 1:
        user_input = input("Guess which number I chose, from 0-10 inclusive. Type exit to quit.")
        random_number = random.randrange(0,11)
        count = 0
        try:
            int(user_input)
        except ValueError as err:
            if user_input == "exit":
                break
            else:
                print("That's not a valid response, try again.")
                continue
        else:
            while 1==1:
                if int(user_input) > random_number:
                    user_input = input("Your guess was too high, try again:")
                    count += 1
                    continue
                elif int(user_input) < random_number:
                    user_input = input("Your guess was too low, try again:")
                    count += 1
                    continue
                else:
                    print("You guessed correctly! You got it in "+str(count)+" tries.")
                    break
guessing_game()
