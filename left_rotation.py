#!/bin/python3

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
