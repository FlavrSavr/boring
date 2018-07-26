import numpy as np
from collections import Counter
import collections
import csv
import re

def lottery_analysis():
    counter = 0
    list_counter = 0
    output_list = []
    pre_change_list = []
    post_change_list = []
    raw_list = np.loadtxt(open("/home/rane/testing/winning_numbers.csv", "rb"), dtype='str', delimiter=',')
    string_version = str(raw_list)
    version0 = re.sub(r" [0-9][0-9]'","'",string_version)
    alt_version1 = version0.replace("' '","','")
    alt_version2 = alt_version1.replace("'\n '","','")
    back = eval(alt_version2)
    for element in back:
        if list_counter < 591:
            pre_change_list.append(element)
            list_counter += 1
        elif list_counter >= 591:
            post_change_list.append(element)
            list_counter += 1
    pre_change_str = str(pre_change_list)
    post_change_str = str(post_change_list)
    version1 = post_change_str.replace("'","")
    version2 = version1.replace(" ",",")
    version3 = version2.replace(",,",",")
    version4 = version3.replace(",0",",")
    list_version = eval(version4)
    check = (len(list_version))/5
    if check == 291.0:
        print("Parsed the correct number of elements.")
    else:
        print("Parsed as incorrect number of elements. Expected 291.0, got "+str(check)+".")
    new_dictionary = dict(Counter(list_version))
    for key, value in new_dictionary.items():
        counter += value
    for key, value in new_dictionary.items():
        output_list.append([key,(value/counter)])
    if counter == 1455:
        print("Correct total of numbers returned.")
    else:
        print("Incorrect total of numbers returned. Expected 1455, got "+str(counter)+".")
    with open("/home/rane/testing/post_change_lottery.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)
lottery_analysis()
