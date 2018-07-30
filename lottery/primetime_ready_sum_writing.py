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


def write_winning_number_sums():
    """Writes a CSV file containing drawing dates and winning Powerball sums.

    Args:
        None

    Returns:
        A CSV file where the first column contains drawing dates in YYYY-MM-DD
        format and the second column contains the corresponding sums of winning
        numbers for that Powerball drawing. Please change your directory path
        accordingly if you're not me.

    Raises:
        None

    """

    # Retrieves the matrix of Powerball drawing dates and winning number sums.
    post_change = sum_all_winning_numbers()

    # Writes the aforementioned matrix to a CSV file. If the file exists, it
    # will overwrite it. This is the intended behavior. Analyzing outdated
    # results is not as useful.
    with open(
    "C:\\Users\\Rane\\boring\\lottery\\current_winning_number_sums.csv",
    "w", newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(post_change)


if __name__ == "__main__":
    write_winning_number_sums()
