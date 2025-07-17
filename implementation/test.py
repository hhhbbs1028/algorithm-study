#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY position
#  2. INTEGER_ARRAY velocity
#  3. INTEGER tableLength
#

import math

def calculateTime(position, velocity, tableLength):
    # Write your code here
    # array / array / integer
    mtime = 0
    m = []
    for i in range(len(position)):
        # print(i, "번째")
        if velocity[i]>0:
            time = (tableLength-position[i])/velocity[i]
            m.append(time)
        elif velocity[i]<0:
            time = position[i]/abs(velocity[i])
            m.append(time)
        else:
            # print(i, "velocity 0")
            continue
        mtime = max(mtime, time)

    
    return math.ceil(mtime)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    position_count = int(input().strip())

    position = []

    for _ in range(position_count):
        position_item = int(input().strip())
        position.append(position_item)

    velocity_count = int(input().strip())

    velocity = []

    for _ in range(velocity_count):
        velocity_item = int(input().strip())
        velocity.append(velocity_item)

    tableLength = int(input().strip())

    result = calculateTime(position, velocity, tableLength)

    fptr.write(str(result) + '\n')

    fptr.close()
