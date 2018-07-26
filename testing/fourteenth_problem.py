def remove_duplicates_without_order_easy(my_list):
    return list(set(my_list))


def remove_duplicates_without_order_hard(my_list):
    for element in my_list:
        number = my_list.count(element)
        if number > 1:
            my_list.remove(element)
        else:
            pass
    return my_list


def remove_duplicates_with_order(my_list):
    reversed_list = my_list[::-1]
    for element in reversed_list:
        number = reversed_list.count(element)
        while number > 1:
            reversed_list.remove(element)
            number = reversed_list.count(element)
        else:
            pass
    revised_list = reversed_list[::-1]
    return revised_list


def f7(my_list):
    seen = set()
    seen_add = seen.add
    return [x for x in my_list if not (x in seen or seen_add(x))]


f7([1, 1, 1, 8, 7, 9, 9, 8, 6, 5, 2, 5, 5, 6])
remove_duplicates_with_order([1, 1, 1, 8, 7, 9, 9, 8, 6, 5, 2, 5, 5, 6])
remove_duplicates_without_order_easy([1, 1, 1, 8, 7, 9, 9, 8, 6, 5, 2, 5, 5, 6])
remove_duplicates_without_order_hard([1, 1, 1, 8, 7, 9, 9, 8, 6, 5, 2, 5, 5, 6])



def test_identical_functions(x,y):
    my_list = [3, 3, 4, 4, 4, 3, 2, 21, 3, 5, 6, 676, 5, 4, 3, 2, 2, 45, 56, 77, 3, 6, 7, 8, 8, 3, 4, 5, 6, 9]
    if x(my_list) == y(my_list):
        return "Working properly."
    else:
        return "Not working properly."

test_identical_functions(remove_duplicates_with_order,f7)
