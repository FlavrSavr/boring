import numpy as np
from collections import Counter
import collections
import csv
import re

def first_six_months_lottery_analysis():
    counter = 0
    output_list = []
    raw_list = np.loadtxt(open("/home/rane/testing/post_change_lottery_segments/#1: 10-07-15_to_04-06-16/first_six_months.csv", "rb"), dtype='str', delimiter=',')
    string_version = str(raw_list)
    print(string_version)
    version0 = re.sub(r" [0-9][0-9]'","'",string_version)
    version1 = version0.replace("' '",",")
    version2 = version1.replace("'\n '",",")
    version3 = version2.replace("'","")
    version4 = version3.replace(" ",",")
    version5 = version4.replace(",0",",")
    version6 = version5.replace("[0","[")
    print("*"*100)
    print(version6)
    """
    back = eval(version6)
    new_dictionary = dict(Counter(back))
    for key, value in new_dictionary.items():
        counter += value
    for key, value in new_dictionary.items():
        output_list.append([key,(value/counter)])
    with open("/home/rane/testing/post_change_lottery_segments/first_six_months_analyzed.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)
    """
first_six_months_lottery_analysis()
