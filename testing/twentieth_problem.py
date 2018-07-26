def contained_within():
    my_list = [0,1,2,3,7,9,12,15,20,29,35,36,38]
    x = int(input("Type in a number to determine if it's within my list:"))
    if x in range((my_list[0]),(my_list[-1])):
        return True
    else:
        return False

contained_within()
