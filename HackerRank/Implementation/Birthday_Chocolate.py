#!/bin/python3

#https://www.hackerrank.com/challenges/the-birthday-bar/problem

import sys

def solve(n, s, d, m):
    count = 0
    for i in range(n - m + 1):
        sum = 0
        for j in range(m):
            sum = sum + s[i + j]
        if sum == d:
            count = count + 1
    return count


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)