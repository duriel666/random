#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#


def maximumToys(prices, k):
    prices.sort()
    z = k
    things = 0
    for x in prices:
        z -= x
        if z < 0:
            break
        else:
            k = z
            things += 1
    return things


if __name__ == '__main__':
    n = 7

    k = 50

    prices = [1, 12, 5, 111, 200, 1000, 10]

    result = maximumToys(prices, k)

    print(str(result) + '\n')
