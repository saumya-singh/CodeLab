#!/bin/python3

#https://www.hackerrank.com/challenges/the-hurdle-race/problem

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
max_height = max(height)

if k < max_height:
    value = max_height - k
else:
    value = 0
print(value)