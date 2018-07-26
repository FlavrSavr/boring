def list():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for element in a:
        if element < 5:
            b.append(element)
    print(b)

list()

def list_2():
    x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    y = []
    z = int(float(input()))
    for element in x:
        if element < z:
            y.append(element)
        else:
            pass
    print(y)

list_2()

def list_3():
    c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([element for element in c if element < 5])

list_3()
