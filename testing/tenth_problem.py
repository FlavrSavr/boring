a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def list_comprehension():
    union = (element for element in a if element in b)
    remove_duplicates = set(union)
    return_list = list(remove_duplicates)
    print(return_list)

list_comprehension()
