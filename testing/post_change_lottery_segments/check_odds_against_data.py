import numpy as np
from collections import Counter
import collections
import csv
import re

def check_odds():
    expected_probability = (5/69)
    while 1 == 1:
        numbers_im_looking_for_input = "["+input("Please type in a comma separated list of the numbers you're looking for. Or, type 'quit' to quit. ")+"]"
        if numbers_im_looking_for_input == "[quit]":
            print("Okay, good luck!")
            break
        numbers_im_looking_for = eval(numbers_im_looking_for_input)
        number_of_queries = len(numbers_im_looking_for)

        probability_dictionary = {}
        overall_match = 0

        probability_list = np.loadtxt(open("/home/rane/testing/post_change_lottery.csv", "rb"), delimiter=',')
        for element_list in probability_list:
            probability_dictionary[int(element_list[0])] = element_list[1]

        if number_of_queries >= 1:
            first_probability = probability_dictionary[numbers_im_looking_for[0]]
            first_skew = (first_probability/(1/69))
            if number_of_queries == 1:
                expected_compound_probability =  first_skew*(5/69)

        if number_of_queries >= 2:
            second_probability = probability_dictionary[numbers_im_looking_for[1]]
            second_skew = (second_probability/(1/69))
            if number_of_queries == 2:
                expected_compound_probability = (first_skew*(5/69))*(second_skew*(5/69))

        if number_of_queries >= 3:
            third_probability = probability_dictionary[numbers_im_looking_for[2]]
            third_skew = (third_probability/(1/69))
            if number_of_queries == 3:
                expected_compound_probability = (first_skew*(5/69))*(second_skew*(5/69))*(third_skew*(5/69))

        if number_of_queries >= 4:
            fourth_probability = probability_dictionary[numbers_im_looking_for[3]]
            fourth_skew = (fourth_probability/(1/69))
            if number_of_queries == 4:
                expected_compound_probability = (first_skew*(5/69))*(second_skew*(5/69))*(third_skew*(5/69))*(fourth_skew*(5/69))

        if number_of_queries == 5:
            fifth_probability = probability_dictionary[numbers_im_looking_for[4]]
            fifth_skew = (fifth_probability/(1/69))
            if number_of_queries == 5:
                expected_compound_probability = (first_skew*(5/69))*(second_skew*(5/69))*(third_skew*(5/69))*(fourth_skew*(5/69))*(fifth_skew*(5/69))

        raw_list = np.loadtxt(open("/home/rane/testing/post_change_lottery_segments/raw_winning_numbers_since_2010.csv", "rb"), dtype='str', delimiter=',')
        string_version = str(raw_list)
        version0 = re.sub(r" [0-9][0-9]'","'",string_version)
        version1 = re.sub(r"(?P<name>'.+?')",r"[\g<name>]",version0)
        version2 = version1.replace("'","")
        version3 = version2.replace("\n","")
        version4 = version3.replace(" ",",")
        version5 = version4.replace("[0","[")
        version6 = version5.replace(",0",",")
        actual_drawing = eval(version6)

        print("*"*20)
        for individual_lists in actual_drawing:
            if number_of_queries == 1:
                if numbers_im_looking_for[0] in individual_lists:
                    overall_match += 1
                    print(individual_lists)
                    print("*"*20)

            elif number_of_queries == 2:
                if numbers_im_looking_for[0] in individual_lists and numbers_im_looking_for[1] in individual_lists:
                    overall_match += 1
                    print(individual_lists)
                    print("*"*20)

            elif number_of_queries == 3:
                if numbers_im_looking_for[0] in individual_lists and numbers_im_looking_for[1] in individual_lists and numbers_im_looking_for[2] in individual_lists:
                    overall_match += 1
                    print(individual_lists)
                    print("*"*20)

            elif number_of_queries == 4:
                if numbers_im_looking_for[0] in individual_lists and numbers_im_looking_for[1] in individual_lists and numbers_im_looking_for[2] in individual_lists and numbers_im_looking_for[3] in individual_lists:
                    overall_match += 1
                    print(individual_lists)
                    print("*"*20)

            elif number_of_queries == 5:
                if numbers_im_looking_for[0] in individual_lists and numbers_im_looking_for[1] in individual_lists and numbers_im_looking_for[2] in individual_lists and numbers_im_looking_for[3] in individual_lists and numbers_im_looking_for[4] in individual_lists:
                    overall_match += 1
                    print(individual_lists)
                    print("*"*20)

        print("Matched "+str(overall_match)+" out of 291 drawings.")
        print("Per our analysis, we thought the probability should be "+str(100*expected_compound_probability)+"%, and we found the probability was "+str(100*(overall_match/291))+"%.")
        multiplier = ((overall_match/291)/expected_compound_probability)
        print("That's a difference of "+str(100*((overall_match/291)-expected_compound_probability))+"%, or a multiplier of "+str(multiplier)+".")
        if multiplier > 1:
            print("Nice find!")
        elif multiplier == 1:
            print("Huh. That's odd.")
        else:
            print("Yikes.")
        print("*"*20)
        continue
check_odds()
