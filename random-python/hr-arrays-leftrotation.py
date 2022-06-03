#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


def rotLeft(a, d):
    for i in range(0, d):
        x = a[0]
        a.remove(a[0])
        a.append(x)
    return(a)
    # Write your code here


if __name__ == '__main__':
    d = 4

    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
    print('\n')
