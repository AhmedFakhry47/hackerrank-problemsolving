#!/bin/python3

import copy
import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0]*n 
    max_value = 0
    
    for ls in queries:
        arr[ls[0] - 1] += ls[-1]
        if ls[1] < len(arr):
            arr[ls[1]] -= ls[-1]
    
    itt = 0            
    for elem in arr:
        itt += elem
        if itt > max_value:
            max_value = itt
            
    return max_value
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
