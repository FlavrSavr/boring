import random
import itertools

def possible_combinations():
    valid_count = 0
    number_set = []
    lower_bound = int(input("Type in lower bound for your range."))
    upper_bound = int(input("Type in upper bound for your range."))
    for _ in range(1,70):
        number_set.append(_)
    possibles = itertools.combinations(number_set,r=5)
    for index, element in enumerate(possibles):
        temporary_list = list(element)
        sum = temporary_list[0]+temporary_list[1]+temporary_list[2]+temporary_list[3]+temporary_list[4]
        if lower_bound <= sum <= upper_bound:
            valid_count += 1
    print("From your range restriction, you're working with \
          a 1 in "+str(valid_count)+" chance of guessing the right combination \
          of numbers.")
    print("For reference, that's a(n) "+str(100*(1-(valid_count/11229676)))+"% \
          improvement over your original 1 in 11229676 chance.")
possible_combinations()
