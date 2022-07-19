#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    diagonal = [arr[i][i] for i in range(len(arr))]
    counter_diagonal = [arr[i][~i] for i in range(len(arr))]
    res = sum(diagonal) - sum(counter_diagonal)
    return abs(res)
   
    
    #ls2 = [str(i) for i in  ls1]

      #==

        #ls2 = []

        #for i in ls1:

            #ls2.append(str(i))
           
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()