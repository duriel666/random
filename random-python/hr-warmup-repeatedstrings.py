#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    x = len(s)
    y = 0
    for letter in s:
        if letter == "a":
            y += 1
    counter_1 = round((n/x-int(n/x))*x)
    counter_2 = int(n/x)*y
    s2 = s[:counter_1]
    z = 0
    for letter in s2:
        if letter == "a":
            z += 1
    count = counter_2+z
    return count
    '''if len(s) > 1:
        while len(s) < n:
            s += s
        s = s[:n]
        count = 0
        for letter in s:
            if letter == "a":
                count += 1
    else:
        count = n
    return count'''


if __name__ == '__main__':
    s = "aab"

    n = 882787

    result = repeatedString(s, n)

    print(str(result) + '\n')
