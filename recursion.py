#!/bin/python3

"""
Task
Write a factorial function that takes a positive integer, N as a parameter and prints the result of  N!(N factorial).
"""

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    new_n = n-1;
    return 1 if new_n == 0 else n * factorial(new_n)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
