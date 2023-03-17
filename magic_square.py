#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # since it's 3x3: the summation should be 15 per row/column/diagonal
    # It should contain unique numbers 
    
    '''
    The algorithm will work as follows:
    1- Check if it's magic, if yes return zero
    2- If no, calculate the distance between it and other magic squares of the same size 
    '''
    
    # All known magic squares for 3x3 magic square
    
    all_magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    
    magic = True
    s_copied = [c for c in s]
    for _ in range(2):
        
        for nrow in range(len(s_copied)):
            if not magic: break
                
            if sum(s_copied[nrow]) != 15:
                magic = False
        
        if not magic: break
        s_copied = [list(i) for i in zip(*s_copied)]
    
    
    # if magic already, return 0
    if magic:
        return 0
    
    # Calculate distance between s and every known magic square
    s_flattened  = [f for c in s for f in c]
    minimum_cost = 20000
    
    for magic_s in all_magic_squares:
        cost = sum([abs(i-j) for i,j in zip(s_flattened,magic_s)])
        
        if cost < minimum_cost:
            minimum_cost = cost
    
    return minimum_cost
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
