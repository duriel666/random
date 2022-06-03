#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    sum1 = 0
    sum2 = -sys.maxsize
    for y in range(0, len(arr)-2):
        for x in range(0, len(arr[y])-2):
            sum1 = arr[y][x]+arr[y][x+1]+arr[y][x+2] + \
                arr[y+1][x+1]+arr[y+2][x]+arr[y+2][x+1]+arr[y+2][x+2]
            if sum1 > sum2:
                sum2 = sum1
    return sum2
    # Write your code here


if __name__ == '__main__':
    arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4],
           [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

    result = hourglassSum(arr)

    print(str(result) + '\n')
