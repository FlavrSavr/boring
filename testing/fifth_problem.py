def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    overlapping_list=[element for element in a if element in b]
    unique_set=set(overlapping_list)
    revised_list=list(unique_set)
    print(revised_list)
list_overlap()

    overlapping_list=[element for element in a if a == b]
