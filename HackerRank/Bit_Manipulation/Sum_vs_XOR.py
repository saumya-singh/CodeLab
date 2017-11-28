#!/bin/python3

#https://www.hackerrank.com/challenges/sum-vs-xor/problem

import sys

def solve(n):
    i = 0
    count = 0
    while 2**i < n:
        i += 1
        
    power = i - 1
    
    for i in range(power + 1):
        if n & (1 << i) == 0:
            count += 1
            
    return 2**count

n = int(input().strip())
result = solve(n)
print(result)