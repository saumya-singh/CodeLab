#!/bin/python3

#https://www.hackerrank.com/challenges/counting-valleys/problem

import sys

def noOfValleys(n, s):
    sea_level = 0
    count = 0
    flag = 0
    for i in range(len(s)):
        if s[i] == "U":
            if sea_level < 0 and s[i - 1] == "D" and flag == 0:
                count += 1
                flag = 1
            sea_level += 1
        elif s[i] == "D":
            sea_level -= 1
        if sea_level == 0:
            flag = 0
    return count
    
n = int(input().strip())
s = input().strip()

count = noOfValleys(n, s)
print(count)