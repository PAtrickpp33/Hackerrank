#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    posit, negat, zeros = 0, 0, 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            posit += 1
        else:
            negat += 1
    print(f'{posit/len(arr):.6f}')
    print(f'{negat/len(arr):.6f}')
    print(f'{zeros/len(arr):.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)