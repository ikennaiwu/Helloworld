#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
m = int(first_multiple_input[0])
n = int(first_multiple_input[1])
matrix = []
for _ in range(m):
    matrix_item = input()
    matrix.append(matrix_item)

word_list = []
for i in range(n):
    for j in range(m):
        word_list.append(matrix[j][i])


    
res = ''.join(word_list)
print(re.sub('(?<=[0-9a-zA-Z])+[^0-9a-zA-Z]+(?=[0-9a-zA-Z])',' ',res))
