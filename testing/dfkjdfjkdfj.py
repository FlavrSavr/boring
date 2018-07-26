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

print(str(list(element for element in my_list if element-10 <= response)))
