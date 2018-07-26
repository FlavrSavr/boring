def primality():
    response = int(float(input("Type in an integer and find out if it's prime:")))
    check_list = list(range(2,response))
    result_list = []
    for element in check_list:
        if response%element == 0:
            result_list.append(element)
        else:
            pass
    if result_list == []:
        print("That's a prime number!")
    else:
        print("That's not a prime number. Here are your number's divisors: "+str(result_list))
primality()

new_list = []
count = 0
response = int(input())
my_list = list(range(response,(response+20)))
#for element in my_list:
    #new_list.append(element)
    #count += 1
    #if count == 10:
    #    break
#print(str(new_list))

print(element for element in my_list)
