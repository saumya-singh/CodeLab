#!/bin/python3

#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import sys

def minJumps(n, c):
    i = 0
    count = 0
    while i < len(c) - 1:
        if (len(c) - 1) - i == 1:
            i += 1
            count += 1
            
        elif c[i + 2] == 1:
            i = i + 1
            count += 1
        else:
            i = i + 2
            count += 1
            
    return count

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
min_count = minJumps(n, c)
print(min_count)