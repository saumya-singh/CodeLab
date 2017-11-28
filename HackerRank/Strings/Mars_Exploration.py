#!/bin/python3

#https://www.hackerrank.com/challenges/mars-exploration/problem

import sys

def radiationChange(s):
    count = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] != "S":
            count += 1
        if s[i + 1] != "O":
            count += 1
        if s[i + 2] != "S":
            count += 1
        i += 3
    return count


S = input().strip()
count = radiationChange(S)
print(count)