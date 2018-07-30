import csv
import re
import requests
import itertools
from decimal import *


def retrieve_raw_lottery_data():
    """Returns matrix of Powerball drawing dates and winning combinations.

    Args:
        None

    Returns:
        Matrix containing Powerball drawing dates and winning Powerball
        combinations from 2010-02-03 to present.

    Raises:
        None

    """

    # Fetches NY Powerball's past results CSV and converts it into a matrix.
    with requests.Session() as s:
        results = s.get("https://data.ny.gov/resource/8vkr-v8vh.csv")
        decode = results.content.decode("utf-8")
        raw = csv.reader(decode.splitlines(), delimiter =',')
        original_output = list(raw)

    # Removes timestamps and the entire multiplier column from the matrix.
    for list_element in original_output:
        temp = list_element[0]
        new_date = temp.replace("T00:00:00.000","")
        list_element[0] = new_date
        list_element.remove(list_element[1])

    # Returns the formatted matrix.
    return original_output


def sum_all_winning_numbers():
    """Returns matrix of Powerball drawing dates and winning combination sums.

    Args:
        None

    Returns:
        Two matrices. One matrix contains drawing dates and summed winning
        Powerball numbers that correspond to when the game was a 59 number
        drawing. This matrix is referred to as 'pre_change'. The date range for
        this data is 2010-02-03 to 2015-10-03.

        The second matrix contains drawing dates and summed winning Powerball
        numbers that correspond to when the game was a 69 number drawing. This
        matrix is referred to as 'post_change'. The date range for this data is
        2015-10-07 to present.

    Raises:
        None

    """

    # Retrieves the matrix of Powerball drawing dates and winning combinations.
    original_output = retrieve_raw_lottery_data()

    # Portion of the matrix that corresponds to Powerball's 59 number drawings.
    pre_change = []

    # Portion of the matrix that corresponds to Powerball's 69 number drawings.
    post_change = []

    # Counter ensuring only one copy of the header row appends to 'pre_change'.
    counter = 0

    # Will be used to identify where the split between the 59 num drawing and
    # 69 num drawing occurs.
    correct_index = 0

    # Overwrites the column header 'winning_numbers' with 'winning_number_sum'.
    for index, list_element in enumerate(original_output):
        if index == 0:
            list_element[1] = "winning_number_sum"

        # Identifies which entries belong to Powerball's 69 num drawings. If
        # you're wondering why I didn't just have one enumerate function with
        # all of these if statements below it, it's because nothing gets
        # appended if we don't set our 'correct_index' value before starting to
        # iterate through the list and append elements. I know it's inefficient.
        if list_element[0] == "2015-10-07":
            correct_index = int(index)

    for index, list_element in enumerate(original_output):
        # Overwrites the winning number combination for each drawing date (str)
        # with the sum of the winning numbers for that drawing date (an int).
        if index > 0:
            temporary = list_element[1]
            change1 = temporary.replace(" ",",")
            change2 = str(change1)
            change3 = re.sub(r",[0-9]+$","",change2)
            change4 = ((int(change3[0]+change3[1]))+(int(change3[3]+change3[4]))
            +(int(change3[6]+change3[7]))+(int(change3[9]+change3[10]))
            +(int(change3[12]+change3[13])))
            list_element[1] = change4

        # Isolates matrix entries that belong to Powerball's 69 num drawings.
        if index <= correct_index:
            post_change.append(list_element)

        # Isolates matrix entries that belong to Powerball's 59 num drawings.
        # Also appends headers that match those of the 'post_change' matrix.
        if index > correct_index:
            while counter == 0:
                pre_change.append(['draw_date','winning_number_sum'])
                counter += 1
            pre_change.append(list_element)

    # Uncomment below to return the matrix for 59 number drawings.
    # return pre_change

    # Returns the matrix for 69 number drawings. Comment below to disable.
    return post_change


def tell_me_all_possible_combinations(x):
    """Prints best lottery sum ranges and their edges for post_change matrix.

    Args:
        None

    Returns:
        Sequentially improving ranges and edges for sums of Powerball lottery
        number combinations belonging to the post_change matrix. Intended to
        inform end users of which combination sums are desirable to guess within
        in order to improve odds of correctly guessing the winning combination.

    Raises:
        None

    To Do:
        Verify the number of all possible combinations. Correct value may be
        11238513 as opposed to the current 11229676.

    """

    # A running tracker of improving edges. Edges improve as they approach 0.
    # We start at 1 because that represents a probability of guessing the
    # correct combination completely randomly.
    best_edge = 1

    # Running tracker of the sum range's lower bound that produced our best edge
    best_low = 0

    # Running tracker of the sum range's upper bound that produced our best edge
    best_high = 0

    # Counter for number of combinations that are left when we restrict their
    # sum to a given range.
    valid_count = 0

    # Counter for number of historical Powerball drawings that we'd match if we
    # restricted their sum to a given range.
    historical_range = 0

    possible_low = [] # All possible values for the lower bound of our sum range.

    number_set = [] # All playable numbers for our lottery.

    # A matrix of dates and the sums of winning numbers for historical Powerball
    # drawings. Excludes the Powerball number. Used for finding our
    # 'historical_range'.
    post_change = sum_all_winning_numbers()

    # Populates our 'number_set' with our Powerball numbers, 1-69 (inclusive).
    for _ in range(1,70):
        number_set.append(_)

    # Assembles all unique combinations of 5 numbers from our 'number_set'.
    combinations = itertools.combinations(number_set,r=5)
    combination_list = list(combinations)

    # Populates our 'possible_high' with upper bounds 70-290 (inclusive).
    for _ in range(70,291):
        possible_high.append(_)

    # Lets each thread work with only a single 'lower_bound' value at a time.
    # Necessary to allow processor threads to divide the work between
    # themselves by picking a single 'lower_bound' from __main__'s range, then
    # repeating the work for subsequent 'lower_bound' values as part of distinct
    # work assignments.
    lower_bound = x

    # Instead of calculating 'valid_count', 'historical_range' and 'edge' for
    # all possible ranges, we're going to let each processor thread iterate
    # using all possible upper bounds but only a single lower bound at a time.
    # Be aware that these threads will process the load asynchronously, and as
    # a result, there will be a lot of incorrectly ordered text output that will
    # need to be sifted through.
    for upper_bound in possible_high:
        if (upper_bound-lower_bound) > 0: # If range is not inverted...
            valid_count = 0 # Reset 'valid_count' for new range
            historical_range = 0 # Reset 'historical_range' for new range
            for element in combination_list:
                temporary_list = list(element)
                sum = (temporary_list[0]+temporary_list[1]+temporary_list[2]
                      +temporary_list[3]+temporary_list[4])
                if lower_bound <= sum <= upper_bound:
                    valid_count += 1

            for index, element_list in enumerate(post_change):
                if index > 0:
                    if lower_bound <= int(element_list[1]) <= upper_bound:
                        historical_range += 1

            # Calculates 'remaining_hit_percentage' for this range.
            remaining_hit_percentage = (historical_range/291)

            # Calculates 'remaining_guess_percentage' for this range.
            remaining_guess_percentage = (valid_count/11238513)

            # Only allows edge assignment for non-zero hits/guesses. Edges
            # should approach 0, but an edge of 0 means we have no possible
            # combinations to guess from, which is useless.
            if (remaining_hit_percentage > 0 and
            remaining_guess_percentage > 0):
                edge = remaining_guess_percentage/remaining_hit_percentage

            elif (remaining_hit_percentage == 0 or
            remaining_guess_percentage == 0):
                edge = 1

            # Prints information for a newly crowned 'best_edge'.
            if edge < best_edge:
                print("Valid count is "+str(valid_count)+
                " out of 11229676.")
                print("Remaining guess percentage was "
                +str(remaining_guess_percentage))
                print("Remaining hit percentage was "
                +str(remaining_hit_percentage))
                print("Existing edge was "+str(best_edge)+"%.")
                best_edge = edge + 0
                print("Best edge is now "+str(best_edge)+"%.")
                best_low = lower_bound
                print("Best low is now "+str(best_low)+".")
                best_high = upper_bound
                print("Best high is now "+str(best_high)+".")
                print("*"*40)

    # Prints final 'best_edge' from all combinations whose sum falls within this
    # single 'lower_bound' and any valid 'upper_bound' range.
    print("Best edge using a lower bound of "+str(lower_bound)+" was "+
    str(best_edge)+" resulting from the range "+str(best_low)+" to "+
    str(best_high)+".")
    print("*"*40)


if __name__ == "__main__":
    retrieve_raw_lottery_data()
    sum_all_winning_numbers()
    pool = Pool()
    pool.map(tell_me_all_possible_combinations,range(70,291))
    pool.close()
    pool.join()
