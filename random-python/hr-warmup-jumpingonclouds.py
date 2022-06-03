#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    loc = 0
    jump = 0
    while loc < len(c):
        if loc+2 < len(c) and c[loc+2] == 0:
            loc += 2
            jump += 1
        elif loc+1 < len(c):
            loc += 1
            jump += 1
        else:
            break
    return jump


if __name__ == '__main__':
    n = 7

    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
