import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    index = 0
    
    while index < len(c) - 2 :
        if c[index + 2]:
            index += 1
        else:
            index += 2
        jump += 1
    if index < len(c) - 1:
            jump += 1
    return jump
    
        
#c = int(input(":"))
#n = list(map(int, input(":").rstrip().split()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
