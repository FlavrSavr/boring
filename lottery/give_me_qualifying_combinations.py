import csv
import requests
import itertools
import random
from collections import Counter

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


def give_high_performing_normal_numbers():
    """Returns a list of normal Powerball numbers that perform >= average.

    Args:
        None

    Returns:
        A list of Powerball numbers (as integers) that have an average or above
        average historical draw frequency. Average is defined as a draw
        frequency of 0.0144 (1.44%).

    Raises:
        None

    """

    # Retrieves the matrix of Powerball drawing dates and winning combinations.
    original_output = retrieve_raw_lottery_data()

    # Portion of the list that corresponds to Powerball's 69 number drawing.
    post_change = []

    counter = 0

    # Will be used to identify where the split between the 69 num drawing and
    # 59 num drawing occurs.
    correct_index = 0

    # Contains numbers that perform average or better (>= 0.0144) with respect
    # to draw frequency in the Powerball.
    high_performing_normal_numbers = []

    for index, list_element in enumerate(original_output):

        # Strips the header row, which is not necessary.
        if index == 0:
            original_output.remove(list_element)

        # Identifies which entries belong to Powerball's 26 num drawing.
        if list_element[0] == "2015-10-07":
            correct_index = int(index)

    for index, list_element in enumerate(original_output):

        # Isolates matrix entries that belong to the Powerball's 69 num drawing.
        if index <= correct_index:

            # Appends a list of winning number integers for each
            # drawing to the 'post_change' list for later draw frequency
            # calculation.
            temp = list_element[1]
            post_change.append((int(temp[0]+temp[1])))
            post_change.append((int(temp[3]+temp[4])))
            post_change.append((int(temp[6]+temp[7])))
            post_change.append((int(temp[9]+temp[10])))
            post_change.append((int(temp[12]+temp[13])))

    # Populates a new dictionary with all possible "Powerball" numbers and the
    # number of times they were drawn.
    dictionary = dict(Counter(post_change))

    # Modifies the dictionary in place to reflect draw frequency, not number of
    # times the number was drawn.
    for key, value in dictionary.items():
        counter += value

    dictionary.update((key, (value/counter)) for key, value
    in dictionary.items())

    # Populates the 'output_list' with average or above average performing nums.
    for key, value in dictionary.items():

        if value >= 0.0144:
            high_performing_normal_numbers.append([key, value])

    # Returns the list for average or above average performing numbers.
    return high_performing_normal_numbers


def give_me_qualifying_combinations(x):
    """Prints a requested number of combinations made from high performing nums.

    Args:
        x = Number of combinations you wanted to generate

    Returns:
        'x' number of combinations of five average or above average performing
        normal Powerball numbers. The numbers in each combination are sorted
        from smallest to largest for readability. Intended to be executed from
        a CLI, this function has no file path dependencies.

    Raises:
        None

    """

    # Our list of Powerball numbers that perform average or above average.
    high_performing_numbers = give_high_performing_normal_numbers()

    # The value for our range's lower bound.
    lower_bound = int(input("What's your lower bound? "))

    # The value for our range's upper bound.
    upper_bound = int(input("What's your upper bound? "))

    chosen_combinations = [] # List of randomly selected qualifying combinations

    # Sum of all draw frequencies for normal Powerball numbers that perform
    # average or better (>= 0.0144). Used to find weighted average of draw
    # frequency for high performing numbers.
    qualifying_total = 0

    # Counter that keeps track of the low end of ranges inside our
    # 'normal_dist_dict'.
    running_tab = 0

    # This will be explained later. Wall of comment incoming.
    normal_dist_dict = {}

    # Calculates the total draw frequency for numbers that perform
    # average or better. Used to calculate the weighted average of each high
    # performing number's draw frequency among all high performing numbers.
    for list_element in high_performing_numbers:
            qualifying_total += list_element[1]

    # Establishes a dictionary where tuples are keys, and the high performing
    # normal numbers are the values. Each tuple is the draw frequency for
    # that normal number among high performing numbers, represented as a
    # portion of 0.0 to 1.0. Because we want to use a randomly generated float
    # between 0.0 and 1.0 to select a number, these ranges must be continuous
    # between different normal numbers. That is, they cannot overlap, and
    # cannot all start at 0. So, each tuple essentially has a meaning of:
    # (where last number's frequency left off,
    # where last number's frequency left off + this number's frequency).

    # For example, let's say we had two high performing normal numbers to
    # choose from: 10 and 12. Among their high performing counterparts, 10 has
    # a draw frequency of 0.45 and 12 has a draw frequency of 0.55. Their
    # 'normal_dist_dict' would look like: {(0, 0.4500000000000001): 10,
    # (0.4500000000000001, 1.0): 12}.
    for list_element in high_performing_numbers:

            normal_dist_dict[(running_tab,
            (((list_element[1]/qualifying_total)+0.0000000000000001)+
            running_tab))] = list_element[0]

            running_tab += ((list_element[1]/qualifying_total)+
            0.0000000000000001)

    # Populates our 'chosen_combinations' with our specified number of randomly
    # selected combinations, provided that they satisfy our qualifications.
    for _ in range(1,(x+1)):

        # We'll loop first here so that if a 'potential_combination' doesn't
        # satisfy our requirements, it doesn't count for how many combinations
        # we asked the function to generate.
        while True:

            # Reset 'potential_combination' so that each one starts empty.
            potential_combination = []

            # We need five numbers inside one 'potential_combination', so we'll
            # iterate through a for loop five times.
            for _ in range(1,6):

                # We'll loop again because some conditions require us to throw
                # a number out. Only numbers that satisfy the conditions will
                # break the loop and be used inside a 'potential_combination'.
                while True:

                    # First, we'll select our random number between 0.0 and 1.0.
                    random_number = random.uniform(0.0, 1.0)

                    # Now we'll select the normal number whose range contains
                    # 'random_number'. This is used for selecting high
                    # performing normal Powerball numbers with the
                    # same bias they're drawn with in historical drawings.
                    for key_range, value in normal_dist_dict.items():

                        if key_range[0] <= random_number < key_range[1]:
                            chosen_number = value

                    # We can't have duplicate numbers inside a
                    # 'potential_combination', so we'll restart the while loop
                    # to pick another number if we get a duplicate.
                    if chosen_number in potential_combination:
                        continue

                    # Provided our number isn't already inside our
                    # 'potential_combination', we'll append it and break
                    # the while loop to count against our five times we want
                    # a number added.
                    else:
                        potential_combination.append(chosen_number)
                    break

            # We'll sort the normal numbers in place so that they're easier
            # to read when we go to print them.
            potential_combination.sort()

            # The sum of our potential_combination, used to determine if its
            # within our allowed sum range.
            combination_sum = sum(potential_combination)

            # Provided that our 'potential_combination' has a 'combination_sum'
            # that's within our allowed range, and that our
            # 'potential_combination' hasn't already been chosen, we'll add it
            # to our 'chosen_combinations' list and break the top-level while
            # loop to count against the x number of combinations we want to
            # generate.
            if lower_bound <= combination_sum <= upper_bound:

                if potential_combination not in chosen_combinations:
                    chosen_combinations.append(potential_combination)
                    break

                # If our 'potential_combination' is already in our
                # 'chosen_combinations' list, we'll pass a continue and
                # generate a new 'potential_combination' in its place.
                else:
                    continue

    # Returns our list of chosen combinations (a list of lists).
    return chosen_combinations


def append_powerball_numbers_and_give_results(x):
    """Adds Powerball numbers to normal number combinations and prints results.

    Args:
        x = Number of Powerball numbers you wanted to generate and append to
        your x number of normal number combinations.

        Intended to be synchronized with give_me_qualifying_combinations(x) by
        using the same arg variable. Theoretically, you want the same amount of
        Powerball numbers as you have combinations.

    Returns:
        x number of user-requested Powerball combinations, with Powerball
        numbers appended, printed to the screen for playing. Only historically
        average or above average performing Powerball numbers are selected, and
        their real, in-game bias is used for their selection in this function.

    Raises:
        None

    """

    # Retrieves the matrix of Powerball drawing dates and winning combinations.
    original_output = retrieve_raw_lottery_data()

    # Portion of the matrix that corresponds to Powerball's 35+ number drawing.
    pre_change_powerball = []

    # Portion of the matrix that corresponds to Powerball's 26 number drawing.
    post_change_powerball = []

    # Counter used to identify how many qualifing drawings have occurred.
    powerball_counter = 0

    # Will be used to identify where the split between the 26 num drawing and
    # 35+ num drawing occurs.
    correct_index = 0

    # Contains Powerball numbers and the frequency that they're drawn.
    output_list = []

    # Sum of all draw frequencies for Powerball numbers that perform average or
    # better (>= 0.038). Used to find weighted average of draw frequency for
    # high performing numbers.
    qualifying_total = 0

    # Counter that keeps track of the low end of ranges inside our
    # 'powerball_dist_dict'.
    running_tab = 0

    # This will be explained later. Wall of comment incoming.
    powerball_dist_dict = {}

    # List of characters to replace in final output.
    replace_dictionary = {"[": "", "]": ""}

    # Retrieves the chosen combinations of normal Powerball numbers.
    chosen_combinations = give_me_qualifying_combinations(x)

    for index, list_element in enumerate(original_output):

        # Strips the header row, which is not necessary.
        if index == 0:
            original_output.remove(list_element)

        # Identifies which entries belong to Powerball's 26 num drawing.
        if list_element[0] == "2015-10-07":
            correct_index = int(index)

    for index, list_element in enumerate(original_output):

        # Overwrites the winning number combination for each drawing date (str)
        # with the "Powerball" number for that drawing date (an int).
        temporary = list_element[1]
        change1 = temporary.replace(" ",",")
        change2 = (int(change1[15]+change1[16]))
        list_element[1] = change2

        # Isolates matrix entries that belong to Powerball's 26 num drawing.
        if index <= correct_index:
            post_change_powerball.append(list_element[1])

    # Populates a new list with all possible post change Powerball numbers and
    # their draw frequency.
    powerball_dictionary = dict(Counter(post_change_powerball))

    for key, value in powerball_dictionary.items():
        powerball_counter += value

    for key, value in powerball_dictionary.items():
        output_list.append([key,(value/powerball_counter)])

    # Calculates the total draw frequency for numbers that perform
    # average or better. Used to calculate the weighted average of each high
    # performing number's draw frequency among all high performing numbers.
    for list_element in output_list:

        if list_element[1] >= 0.038:
            qualifying_total += list_element[1]

    # Establishes a dictionary where tuples are keys, and the high performing
    # Powerball numbers are the values. Each tuple is the draw frequency for
    # that Powerball number among high performing numbers, represented as a
    # portion of 0.0 to 1.0. Because we want to use a randomly generated float
    # between 0.0 and 1.0 to select a number, these ranges must be continuous
    # between different Powerball numbers. That is, they cannot overlap, and
    # cannot all start at 0. So, each tuple essentially has a meaning of:
    # (where last number's frequency left off,
    # where last number's frequency left off + this number's frequency).

    # For example, let's say we had two high performing Powerball numbers to
    # choose from: 10 and 12. Among their high performing counterparts, 10 has
    # a draw frequency of 0.45 and 12 has a draw frequency of 0.55. Their
    # 'powerball_dist_dict' would look like: {(0, 0.4500000000000001): 10,
    # (0.4500000000000001, 1.0): 12}.
    for list_element in output_list:

        if list_element[1] >= 0.038:
            powerball_dist_dict[(running_tab,
            (((list_element[1]/qualifying_total)+0.0000000000000001)+
            running_tab))] = list_element[0]

            running_tab += ((list_element[1]/qualifying_total)+
            0.0000000000000001)


    for list_element in chosen_combinations:

        # Selects our random number between 0.0 and 1.0 so we can choose a
        # Powerball number.
        random_number = random.uniform(0.0, 1.0)

        # Picks the Powerball number that has the range 'random_number' belongs
        # within. Used for selecting high performing Powerball numbers with the
        # same bias that they have in historical drawings.
        for key_range, value in powerball_dist_dict.items():
            if key_range[0] <= random_number < key_range[1]:

                # Number chosen for this combination.
                chosen_number = value
                list_element.append(chosen_number)

    print("*"*37)
    print("Here are your requested combinations:")
    print("*"*37)

    # Remove the brackets around each 'combination_list' inside
    # our 'chosen_combinations' list so that they display more elegantly,
    # then print each 'combination_list'.
    for element_list in chosen_combinations:

        temp = str(element_list)
        for initial, edit in replace_dictionary.items():

            temp = temp.replace(initial, edit)
        print(temp)

    print("*"*37)
    print("Good luck!")
    print("*"*37)


if __name__ == "__main__":
    append_powerball_numbers_and_give_results(int(input("How many combinations would "+
    "you like to play? ")))
