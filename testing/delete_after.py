import numpy as np
from collections import Counter
import collections
import csv
import re


def lottery_analysis():
    counter = 0
    output_list = []
    raw_list = np.loadtxt(open("/home/rane/testing/winning_numbers.csv", "rb"), dtype='str', delimiter=',')
    string_version = str(raw_list)
    #print(string_version)
    version0 = re.sub(r" [0-9][0-9]'","'",string_version)
    print(version0)
    """
    version1 = version0.replace("[","")
    version2 = version1.replace("'","")
    version3 = version2.replace(" ",",")
    version4 = version3.replace("\n","")
    version5 = version4.replace("]","")
    version6 = version5.replace("01,10,27,28,36,12","01,10,27,28,36,12]")
    version7 = version6.replace("17,22,36,37,52","[17,22,36,37,52")
    version8 = version7.replace(",0",",")
    list_version = eval(version8)
    new_dictionary = dict(Counter(list_version))
    for key, value in new_dictionary.items():
        counter += value
    for key, value in new_dictionary.items():
        output_list.append([key,(value/counter)])
    with open("/home/rane/testing/formatted_lottery.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)
    """
lottery_analysis()
