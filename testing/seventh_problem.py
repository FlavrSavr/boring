def list_comprehension():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [element for element in a if (element%2) == 0]
    print(b)
list_comprehension()player_1_input = print(input("Please enter either rock, paper or scissors:"))
player_2_input = print(input("Please enter either rock, paper or scissors:"))
