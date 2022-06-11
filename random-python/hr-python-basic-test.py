#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    result=0
    neighbor=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c=0
            for x in neighbor:
                y=x[0]
                z=x[1]
                try:
                    if grid[i][j]<=grid[i+y][j+z] and i+y>-1 and j+z>-1:
                        c+=1
                except:
                    pass
            if c==0:
                result+=1
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
