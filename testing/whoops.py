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
            if int(user_input) > random_number:
                user_input_int = input("Your guess was too high, try again:")
                count += 1
                break
            elif int(user_input) < random_number:
                user_input = input("Your guess was too low, try again:")
                count += 1
                break
            else:
                print("You guessed correctly! You got it in "+str(count)+" tries.")
guessing_game()
