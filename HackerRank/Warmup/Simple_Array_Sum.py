#!/bin/python3

#https://www.hackerrank.com/challenges/simple-array-sum/problem

import sys

def simpleArraySum(n, ar):
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)