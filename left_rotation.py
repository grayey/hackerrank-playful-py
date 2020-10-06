#!/bin/python3

"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d, perform d left rotations on the array.
 Return the updated array to be printed as a single line of space-separated integers.

"""

import math
import os
import random
import re
import sys
from collections import deque;

# Complete the rotLeft function below.
def rotLeft(a, d):
    count_rotations = 0;
    array_length = len(a);
    dequed = deque(a);
    while count_rotations < d:
        dequed.insert(array_length-1, dequed.popleft());
        count_rotations += 1
    return dequed;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
