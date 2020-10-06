#!/bin/python3

"""
Task
Given an integer, n, print its first 10 multiples. 
Each multiple  n X i (where i <= N <= 10) should be printed on a new line in the form: n x i = result.

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        output = f"{str(n)} x {str(i)} = {str(n*i)}"
        print(output)

