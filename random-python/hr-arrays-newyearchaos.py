#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    total = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                total += 1
                q[i], q[i-1] = q[i-1], q[i]
            elif q[i-2] == i+1:
                total += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i], q[i-1] = q[i-1], q[i]
            else:
                print("Too chaotic")
                return
    print(total)

    '''bribe = 0
    total = 0
    chaos = False
    for i in range(0, len(q)):
        x = q[i]
        if x > i+1:
            bribe = x-i-1
            if bribe > 2:
                chaos = True
            total += bribe
    if chaos:
        print("Too chaotic")
    elif not chaos:
        print(total)'''


if __name__ == '__main__':
    q = [2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10, 14, 13, 12, 17, 16, 15]

    minimumBribes(q)
