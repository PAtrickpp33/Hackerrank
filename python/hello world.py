print("Hello, World!")

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif n%2==0 and n in range(2,6):
        print("Not Weird")
    elif n%2==0 and n in range(6,21):
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")



if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print (a+b)
    print (a-b)
    print (a*b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

if __name__ == '__main__':
    n = int(input())
    [print(i**2) for i in range(n)]

def is_leap(year):
    leap = False
    
    # Write your logic here
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
    

year = int(input())


if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        
        print (i+1,end='')