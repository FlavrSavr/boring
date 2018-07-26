import random
def cows_and_bulls_debug():
    guess_count = 1
    my_number = []
    for _ in range(4):
        my_number.append(str(random.randint(0,9)))
    user_input = list(input("My number is "+("".join(my_number))+". Type your guess: "))
    while user_input != my_number:
        preserved_user_input = user_input[:]
        remaining_numbers = my_number[:]
        print("To begin, my number is "+("".join(remaining_numbers)))
        print("*"*55)
        cow_count = 0
        bull_count = 0
        try:
            int("".join(user_input))
        except (ValueError) as err:
            break
        else:
            for position,element in enumerate(user_input):
                if user_input[position] == my_number[position]:
                    cow_count += 1
                    print("User input is "+("".join(user_input)))
                    print("Number referenced in user input is "+(str(user_input[position]))+" at position "+(str(position)))
                    print("Number referenced in my number is "+(str(my_number[position]))+" at position "+(str(position)))
                    print("Cow count is now "+str(cow_count))
                    remaining_numbers[position] = "@"
                    user_input[position] = "!"
                    print("Remaining numbers are "+("".join(remaining_numbers)))
                    print("*"*55)
            for position,element in enumerate(user_input):
                if element in remaining_numbers:
                    bull_count += 1
                    print("User input is "+("".join(user_input)))
                    print("Number referenced in user input is "+(str(user_input[position]))+" at position "+(str(position)))
                    print("Bull count is now "+str(bull_count))
                    remaining_numbers.remove(element)
                    remaining_numbers.append("@")
                    user_input[position] = "!"
                    print("Remaining numbers are "+("".join(remaining_numbers)))
                    print("*"*55)
        user_input = list(input("Not quite, that's "+str(bull_count)+" bull(s) and "+str(cow_count)+" cow(s). Try again with a new guess. \
                                Your last guess was "+("".join(preserved_user_input))+". My number is still "+("".join(my_number))+". "))
        guess_count += 1
        continue
    if user_input == my_number and guess_count == 1:
        print("*"*55)
        print("You got it on the first try? C'mon, nobody likes a cheater.")
    elif user_input == my_number and guess_count > 1:
        print("*"*55)
        print("Good job, you got it in "+str(guess_count)+" guesses!")


if __name__ == "__main__":
    cows_and_bulls_debug()
