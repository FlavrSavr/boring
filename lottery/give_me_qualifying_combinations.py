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


def give_high_performing_numbers():
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
    high_performing_numbers = []

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
            high_performing_numbers.append(key)

    # Returns the list for average or above average performing numbers.
    return high_performing_numbers


def give_me_qualifying_combinations(x):
    """Prints a requested number of combinations made from high performing nums.

    Args:
        x = Number of combinations you want to generate

    Returns:
        'x' number of combinations of five average or above average performing
        normal Powerball numbers. The numbers in each combination are sorted
        from smallest to largest for readability. Intended to be executed from
        a CLI, this function has no file path dependencies.

    Raises:
        None

    """

    # Our list of Powerball numbers that perform average or above average.
    high_performing_numbers = give_high_performing_numbers()

    # The value for our range's lower bound.
    lower_bound = int(input("What's your lower bound? "))

    # The value for our range's upper bound.
    upper_bound = int(input("What's your upper bound? "))

    chosen_combinations = [] # List of randomly selected qualifying combinations

    replace_dictionary = {"[": "", "]": ""} # List of characters to replace.

    # Assembles all possible unique combinations of 5 numbers from our
    # 'high_performing_numbers' list.
    combination_list = list(itertools.combinations(high_performing_numbers,r=5))

    # Populates our 'chosen_combinations' with our specified number of randomly
    # selected combinations, provided that they satisfy our qualifications.
    for _ in range(1,(x+1)):
        while True:
            potential_combination = list(random.choice(combination_list))
            potential_combination.sort()
            combination_sum = sum(potential_combination)
            if lower_bound <= combination_sum <= upper_bound:
                if potential_combination not in chosen_combinations:
                    chosen_combinations.append(potential_combination)
                    break
                else:
                    continue
            else:
                continue

    print("*"*37)
    print("Here are your requested combinations:")
    print("*"*37)

    # Replace the list format of each combination
    for element_list in chosen_combinations:
        temp = str(element_list)
        for initial, edit in replace_dictionary.items():
            temp = temp.replace(initial, edit)
        print(temp)

    print("*"*37)
    print("Good luck!")
    print("*"*37)

if __name__ == "__main__":
    give_me_qualifying_combinations(int(input("How many combinations would "+
    "you like to play? ")))
