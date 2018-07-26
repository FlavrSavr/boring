import random
random.__builtins__
random.randint(20,50)

def get_me_a_random_integer():
    print random.randint(0,100)

get_me_a_random_integer()

def get_random_integer():
    return random.randint(0,80000)

get_random_integer()

import sys
print(sys.maxsize, sys.maxsize+1)
import numpy as np

print (sys.float_info.max)
print (6.023e23)
print (9/3)
print (9//3)
print (64%8)
print (100//8, 100%8)


def cockblockula():
    return (7**(1//2))*(4/3)<(((3**2)*(3/4))/(1+2**2))

cockblockula()

array1 = np.random.randint(-100,100, size=(5,5),dtype=np.int8)
print(array1)
print(-1*array1)
array2 = np.random.randint(-50,500, size=(5,5))
print (array2)
print (array1*array2)
16*229
help(np.maximum)
help(np.uint8)

print("*"*40)
print("*"*40)
print("*"*40)
import os
import numpy as np
import numpy.random as ra
import pandas as pd
pd.__version__
help(np.array)
np.array([0,1,2,3])
np.array([[1, 2, 6, 8], [8, 9, 5, 4]])













def this_is_a_function(this):
    try:
        x = int(this)
    except ValueError:
        try:
            y = float(this)
        except ValueError:
            print ("That's a string, try something else.")
            this_is_a_function(input())
        else:
            print ("That's a float, try something else.")
            this_is_a_function(input())
    else:
        print("That's what I was looking for, good job.")
        return
print("Type something in.")
this_is_a_function(input())
#
