import numpy as np
import re

def data_cleanup():
    best_edge_list_int = []
    best_edge_list_fin = []
    with open('RESULTS.txt', 'r') as file:
        data = file.readlines()

    for line in data:
        if "Best edge was" in line:
            best_edge_list_int.append(line)

    for element in best_edge_list_int:
        modified = element.replace("\n","")
        if "edge was 1" not in modified:
            best_edge_list_fin.append(modified)

    best_edge_list_fin.sort()

    output_file = open("RESULTS_ANALYZED.txt","w")

    for element in best_edge_list_fin:
        output_file.write(element+"\n")

data_cleanup()
