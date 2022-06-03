#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    list = ar
    pareja = 0
    for x in range(0, len(list)):
        num1 = list[x]
        print(str(num1)+" x")
        list[x] = "x"
        for y in range(0, len(list)):
            num2 = list[y]
            print(str(num2)+" y")
            if num1 == num2 and not num1 == "x" and not num2 == "x":
                pareja += 1
                print(list)
                list[y] = "x"
                print(list)
                break
    print(list)
    return pareja


if __name__ == '__main__':

    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
