#!/bin/python3

#https://www.hackerrank.com/challenges/camelcase/problem

import sys

def camelCase(s):
    count = 0
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            count += 1
    return count + 1

s = input().strip()
count = camelCase(s)
print(count)