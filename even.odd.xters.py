# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed 
characters as 2 space-separated strings on a single line.

"""


import fileinput
input_lines = fileinput.input()

for idx, line in enumerate(input_lines):
    if idx == 0:
        continue;
    left = ''
    right = ''
    for ix, xter in enumerate(line.rstrip()):
        if ix%2:
            right+=xter;
        else:
            left+=xter;
    output = f"{left} {right}"
    print(output)