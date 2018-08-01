import random
import csv
import requests
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


def write_powerball_numbers():
    """Writes a CSV file of "Powerball" numbers and their draw distribution.

    Args:
        None

    Returns:
        A CSV file where the first column contains each "Powerball" number
        and the second column contains the corresponding draw distribution
        for that number. Please update your directory path accordingly if you're
        not me.

    Raises:
        None

    """

    # Retrieves the matrix of Powerball drawing dates and winning combinations.
    original_output = retrieve_raw_lottery_data()

    # Portion of the matrix that corresponds to Powerball's 35+ number drawing.
    pre_change_powerball = []

    # Portion of the matrix that corresponds to Powerball's 26 number drawing.
    post_change_powerball = []

    # Counter ensuring only one copy of the header row appends to
    # 'pre_change_powerball'.
    counter = 0

    # Counter used to identify how many qualifing drawings have occurred.
    powerball_counter = 0

    # Will be used to identify where the split between the 26 num drawing and
    # 35+ num drawing occurs.
    correct_index = 0

    # Contains Powerball numbers and the frequency that they're drawn.
    output_list = []

    for index, list_element in enumerate(original_output):

        # Strips the header row, which is not necessary.
        if index == 0:
            original_output.remove(list_element)

        # Identifies which entries belong to Powerball's 26 num drawing.
        if list_element[0] == "2015-10-07":
            correct_index = int(index)

    # Overwrites the winning number combination for each drawing date (str)
    # with the "Powerball" number for that drawing date (an int).
    for index, list_element in enumerate(original_output):
        temporary = list_element[1]
        change1 = temporary.replace(" ",",")
        change2 = (int(change1[15]+change1[16]))
        list_element[1] = change2

        # Isolates matrix entries that belong to Powerball's 26 num drawing.
        if index <= correct_index:
            post_change_powerball.append(list_element[1])

        # Isolates matrix entries that belong to Powerball's 35+ num drawings.
        if index > correct_index:
            pre_change_powerball.append(list_element[1])

    # Populates a new list with all possible "Powerball" numbers and their
    # draw frequency.
    powerball_dictionary = dict(Counter(post_change_powerball))

    for key, value in powerball_dictionary.items():
        powerball_counter += value

    for key, value in powerball_dictionary.items():
        output_list.append([key,(value/powerball_counter)])

    # Writes 'output_list' draw distribution matrix to a CSV file. If the file
    # exists, it will overwrite it. This is the intended behavior. Analyzing
    # outdated results is not as useful.
    with open(
    "C:\\Users\\Rane\\boring\\lottery\\post_change_powerball_number_analysis.csv",
    "w", newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(output_list)


if __name__ == "__main__":
    write_powerball_numbers()
