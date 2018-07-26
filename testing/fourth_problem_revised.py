def divisors():
    print("Enter any number to identify its positive integer divisors. Keep the number small if you want a quick response.")
    response = int(input())
    my_list = []
    range_list = list(range(1,response+1))
    if response > 0:
        updated_list =[element for element in range_list if response%element == 0]
    else:
        print("That number isn't a positive, non-zero number.")
    print(updated_list)
divisors()
