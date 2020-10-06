#!/bin/python3

"""
Task
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    output = "";
    for letter in arr:
        output+= f"{str(letter)} ";
    print(output.rstrip())

