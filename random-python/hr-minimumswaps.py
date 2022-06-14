'''def minimumSwaps(arr, n, swaps=0):
    # iterate over entire array
    for i in range(0, n):
        # it's good practice to use a boolean guided function in a long for loop,
        # while will evaluate and IF the statement in it is true it will continue
        # I used the consecutive, increasing values to swap by index
        while arr[i] != (i+1):
            # temp is the correct index of arr[i]
            temp = arr[i]-1
            # swap this with whatever element is where arr[temp] is, this will
            # continue to swap until arr[i] == index+1
            arr[i], arr[temp] = arr[temp], arr[i]
            # increase swaps
            swaps += 1
    return swaps'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    arr2 = sorted(arr)
    value = 0
    for i in range(len(arr)-1):
        while arr[i] != arr2[i]:
            temp = arr[i]-1
            arr[i], arr[temp] = arr[temp], arr[i]
            value += 1
    return value


if __name__ == '__main__':
    n = 5
    arr = [2, 3, 4, 1, 5]
    res = minimumSwaps(arr)
    print(str(res) + '\n')
