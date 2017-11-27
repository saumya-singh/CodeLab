#!/bin/python3

#https://www.hackerrank.com/challenges/kangaroo/problem

import sys

def kangaroo(x1, v1, x2, v2):
    n = x2 - x1
    d = v1 - v2
    if d == 0 and n == 0:
        return "YES"
    if d == 0 and n != 0:
        return "NO"
    t = n/d
    mod = n % d
    if t > 0 and mod == 0:
        return "YES"
    else:
        return "NO"
        

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)