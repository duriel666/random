#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def twoStrings(s1, s2):
    # Write your code here
    for x in s1:
        z = s2.find(x)
        if z > -1:
            return"YES"
    return "NO"
    


if __name__ == '__main__':
    q = 1

    for q_itr in range(q):
        s1 = "aardvark"

        s2 = "apple"

        result = twoStrings(s1, s2)

        print(result + '\n')
