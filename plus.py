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

    pos = 0
    neg = 0
    zero = 0

    for num in range(n):
        if num>=0:
            if num==0:
                zero += 1
            else:
                pos += 1
        else:
            neg += 1

    pos = pos/n
    neg = neg/n
    zero = zero/n
    print('%.4f'%pos)
    print('%.4f'%neg)
    print('%.4f'%zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

6
-4 2 -9 0 4 1