#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    level = 0
    level1 = 0
    valley = 0
    for x in path:
        if x == "U":
            level += 1
        elif x == "D":
            level -= 1
        if level >= 0 and level1 < 0:
            valley += 1
        level1 = level
    return valley


if __name__ == '__main__':

    steps = 8

    path = "UDDDUDUU"

    result = countingValleys(steps, path)

    print(str(result) + '\n')
