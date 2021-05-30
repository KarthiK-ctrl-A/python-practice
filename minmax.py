import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minsum = 0
    maxsum = 0
    minele = min(arr)
    maxele = max(arr)
    s = sum(arr)
    minsum = s - maxele
    maxsum = s - minele
    print(minsum, maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
