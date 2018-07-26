import random
def cows_and_bulls():
    guess_count = 0
    my_number = []
    for _ in range(4):
        my_number.append(str(random.randint(0,9)))
    user_input = list(input("Type your guess below. "))
    preserved_user_input = user_input[:]
    while user_input != my_number:
        remaining_numbers = my_number[:]
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
                    remaining_numbers[position] = "@"
                    user_input[position] = "!"
            for position,element in enumerate(user_input):
                if element in remaining_numbers:
                    bull_count += 1
                    remaining_numbers.remove(element)
                    remaining_numbers.append("@")
                    user_input[position] = "!"
        user_input = list(input("Not quite, that's "+str(bull_count)+" bull(s) and "+str(cow_count)+" cow(s). Try again with a new guess. \
                                Your last guess was "+(" ".join(preserved_user_input))+". "))
        guess_count += 1
        continue
    if user_input == my_number and guess_count == 1:
        print("You got it on the first try? C'mon, nobody likes a cheater.")
    elif user_input == my_number and guess_count > 1:
        print("Good job, you got it in "+str(guess_count)+" guesses!")
cows_and_bulls()


if __name__ == "__main__":
    cows_and_bulls()
















"""
in a python dictionary,

if we call the dictionary "vars"

you can call the associated value using a key:

vars["Key"]

similar to how you would call a list element with its index value

but if you write this in and the key is not present in the dictionary,
you will get an exception: KeyError

however, if you type:
"key" in vars
you will get a True/False response

if you arent sure how the key might be spelled, you can do:
"key" in vars or "Key" in vars or "KEY" in vars
for as many different permutations of your key string you can think to query

-------------
for converting long python strings containing text you can just:
txt =
-------------
from Collections import Counter

Counter() allows you to count the individual elements in a list

if you want to take a string of text, remove the punctuation, and make everything lowercase

you can then split the string (we'll call it into elements of a list using
"""
