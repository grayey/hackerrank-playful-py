#!/bin/python3

'''
Task
Given a base-10 integer, , convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
'''

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input());
    bin_n = bin(n);
    max_1s = 0;
    current = 0;

    for idx, value in enumerate(bin_n):
        if bin_n[idx] == '1':
            current += 1;
            if current > max_1s:
                max_1s = current;
        else: 
            if max_1s >= (len(bin_n) / 2):
                 break;
            current = 0;        
    print(max_1s);