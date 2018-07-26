import numpy as np
from collections import Counter
import collections
import csv
import re
import random

def working():
    intermediate_list = []
    output_list = []
    raw_list = np.loadtxt(open("/home/rane/Downloads/processing.csv", "rb"), dtype='float', delimiter=',')
    intermediate_list = raw_list.tolist()
    new_dictionary = dict(Counter(intermediate_list))
    for key, value in new_dictionary.items():
        output_list.append((key,value))
    with open("/home/rane/Downloads/processed.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)
working()

def big_random():
    number_list = []
    sample_output = []
    temporary_list = []
    intermediate = []
    counter = 0
    dict_counter = 0
    for element in range(1,70):
        number_list.append(element)
    while counter < 1000:
        temporary_list = random.sample(number_list,5)
        for element in temporary_list:
            intermediate.append(element)
        counter += 1
    sample_dict = dict(Counter(intermediate))
    for key, value in sample_dict.items():
        dict_counter += value
    for key, value in sample_dict.items():
        sample_output.append((key,(value/dict_counter)))
    with open("/home/rane/testing/small_dataset_r_5.csv","w") as file:
        writer = csv.writer(file)
        writer.writerows(sample_output)
big_random()
