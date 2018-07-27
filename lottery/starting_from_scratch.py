import numpy as np
from collections import Counter
import collections
import csv
import re
import pandas as pd
from sodapy import Socrata
import requests
import itertools
from decimal import *


def retrieve_raw_lottery_data():
    """This pulls the most updated copy of the winning numbers list from the NY
    government's Powerball API, strips the timestamp and multiplier
    information (but not the datestamp), and returns a list of lists. Each list
    in the list has the following format:

    [['draw_date', 'winning_numbers'], ... ,['2010-02-03', '17 22 36 37 52 24']]

    This returns Powerball drawings from 2010 onwards, NOT from when the game
    changed in 2015. For your reference, the first date in which the
    modified 69-number game was played was '2015-10-07'. Any drawings from '2015-10-03'
    and earlier were in the earlier 59-number format. Dates in this dataseries are
    always in YYYY/MM/DD format.

    To reference this data in subsequent functions, you can call it with the
    variable 'original_output'."""

    with requests.Session() as s:
        results = s.get("https://data.ny.gov/resource/8vkr-v8vh.csv?$$app_token=vjxekB7YMF1tZ0e8Oz7cFezDP")

        decode = results.content.decode("utf-8")
        raw = csv.reader(decode.splitlines(), delimiter =',')
        original_output = list(raw)

    for list_element in original_output:
        temp = list_element[0]
        new_date = temp.replace("T00:00:00.000","")
        list_element[0] = new_date
        list_element.remove(list_element[1])

    return original_output


def sum_all_winning_numbers():
    """This takes the string version of the six winning numbers, removes
    the powerball number, turns the remaining five numbers into
    integers and then sums all the integers for each individual drawing.

    Afterwards, it overwrites the value for 'winning_numbers' in the
    ['draw_date','winning_numbers'] list with the sum, resulting in
    the format ['draw_date',winning_number_sum].

    It then splits this list of lists into two separate master lists: one that corresponds
    to before the game changed, and one that corresponds to after the game changed.

    Finally, each of these modified list of lists is returned as a variable
    for downstream use: 'pre_change' corresponds to drawings from
    2010-02-03 to 2015-10-03, while 'post_change' corresponds to drawings from
    2015-10-07 to present."""

    original_output = retrieve_raw_lottery_data()
    pre_change = []
    post_change = []
    counter = 0

    for index, list_element in enumerate(original_output):
        if index == 0:
            list_element[1] = "winning_number_sum"

        if index > 0:
            temporary = list_element[1]
            change1 = temporary.replace(" ",",")
            change2 = str(change1)
            change3 = re.sub(r",[0-9]+$","",change2)
            change4 = ((int(change3[0]+change3[1]))+(int(change3[3]+change3[4]))+(int(change3[6]+change3[7]))+(int(change3[9]+change3[10]))+(int(change3[12]+change3[13])))
            list_element[1] = change4

        if index < 292:
            post_change.append(list_element)

        if index >= 292:
            while counter == 0:
                pre_change.append(['draw_date','winning_number_sum'])
                counter += 1
            pre_change.append(list_element)

    return pre_change
    return post_change


def tell_me_all_possible_combinations():
    """Populates a list with all possible combinations of five numbers,
    without replacement, from a pool of numbers ranging from 1-69 (inclusive).

    Each combination in this list is then summed and compared to a range of
    allowable sums. If this combination's sum is within the range, 1 is added to
    a counter. This counter is cumulative for all 11,000,000+ combinations
    being summed and compared within a single range. Between different ranges,
    counters are distinct and separate.

    This summing, range comparison and counting is repeated for all possible
    ranges with a lower bound between 70-289 and an upper bound between 71-290.
    Ranges must be positive, e.g. 70-71 is okay, but 71-70 is not.

    The ratio of (# of combination sums that fit within the range)/
    (# of combination sums) yields a percentage which we call
    'remaining_guess_percentage'. This is the percentage of all possible
    combinations that are included if we only allow combinations with a sum
    that falls within the given range.

    This is then compared to a calculated ratio of
    (# of historical Powerball drawing sums that fall within our above range)/
    (# of all historical Powerball drawing sums), which we call
    'remaining_hit_percentage'.

    Essentially, as (remaining_guess_percentage/remaining_hit_percentage)
    approaches 0, we improve our odds of guessing the correct combination if we
    limit our guesses to combinations whose sum falls within the described
    range. We refer to this quotient as our 'edge'.

    So, provided that we're
    guessing within the range that produced our 'edge', we will have improved
    odds which will be calculated and listed alongside our edge and our
    range bounds each time a better edge is produced for a given lower bound.

    Once all combinations' sums for all possible ranges have been iterated
    through, a final statement is printed with the best possible edge and its
    corresponding bounds and probability."""

    best_edge = 1
    best_low = 0
    best_high = 0
    valid_count = 0
    historical_range = 0
    possible_low = []
    number_set = []
    post_change = sum_all_winning_numbers()

    for _ in range(1,70):
        number_set.append(_)

    combinations = itertools.combinations(number_set,r=5)
    combination_list = list(combinations)

    for _ in range(70,291):
        possible_low.append(_)

    possible_high = possible_low[:]

    for element1 in possible_low:
        for element2 in possible_high:
            if (element2-element1) > 0:
                valid_count = 0
                historical_range = 0
                for element in combination_list:
                    temporary_list = list(element)
                    sum = temporary_list[0]+temporary_list[1]+temporary_list[2]+temporary_list[3]+temporary_list[4]
                    if element1 <= sum <= element2:
                        valid_count += 1

                for index, element_list in enumerate(post_change):
                    if index > 0:
                        if element1 <= int(element_list[1]) <= element2:
                            historical_range += 1

                remaining_hit_percentage = (historical_range/291)
                remaining_guess_percentage = (valid_count/11229676)

                if remaining_hit_percentage > 0 and remaining_guess_percentage > 0:
                    edge = remaining_guess_percentage/remaining_hit_percentage

                elif remaining_hit_percentage == 0 or remaining_guess_percentage == 0:
                    edge = 1

                if edge < best_edge:
                    print("Valid count is "+str(valid_count)+" out of 11229676.")
                    print("Remaining guess percentage was "+str(remaining_guess_percentage))
                    print("Remaining hit percentage was "+str(remaining_hit_percentage))
                    print("Existing edge was "+str(best_edge)+"%.")
                    best_edge = edge + 0
                    print("Best edge is now "+str(best_edge)+"%.")
                    best_low = element1
                    print("Best low is now "+str(best_low)+".")
                    best_high = element2
                    print("Best high is now "+str(best_high)+".")
                    print("*"*40)

    print("Best edge was "+str(best_edge)+" resulting from the range "+str(best_low)+" to "+str(best_high)+".")
    print("*"*40)


def tell_me_combinations_within_range():
    valid_count = 0
    historical_range = 0
    number_set = []
    lower_bound = int(input("Type in lower bound for your range."))
    upper_bound = int(input("Type in upper bound for your range."))
    post_change = sum_all_winning_numbers()

    for _ in range(1,70):
        number_set.append(_)

    possibles = itertools.combinations(number_set,r=5)

    for index, element in enumerate(possibles):
        temporary_list = list(element)
        sum = temporary_list[0]+temporary_list[1]+temporary_list[2]+temporary_list[3]+temporary_list[4]
        if lower_bound <= sum <= upper_bound:
            valid_count += 1

    for index, element_list in enumerate(post_change):
        if index > 0:
            if lower_bound <= int(element_list[1]) <= upper_bound:
                historical_range += 1

    getcontext().prec = 4
    random_guess_chance = (100*((1/Decimal(valid_count))*(Decimal(historical_range)/291)))
    guess_within_range_chance = (100*(1/(Decimal(valid_count))))

    print("If we assume that you're guessing randomly, you've got a "+
    str(random_guess_chance)+"% chance of guessing the right combination."+
    "\nCompared to your original 0.0000089% chance, that's a(n) "
    +str(random_guess_chance/Decimal(0.0000089))+"x improvement!")

    print("*"*100)

    print("If we assume that you're only guessing inside your desired range,"+
    " you've got a "+str(guess_within_range_chance)+"% chance of guessing the "+
    "right combination.\nCompared to your original 0.0000089% chance, that's "+
    "a(n) "+str(guess_within_range_chance/Decimal(0.0000089))+"x improvement!")


tell_me_combinations_within_range()
