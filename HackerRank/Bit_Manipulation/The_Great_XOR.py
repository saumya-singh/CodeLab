#!/bin/python3

#https://www.hackerrank.com/challenges/the-great-xor/problem

import sys

def theGreatXor(x):
    count = 0
    i = 0
    while 2 ** i < x:
        i += 1
    power = i
    for i in range(power):
        if x & (1 << i) == 0:
            count += 2 ** i
    return count

q = int(input().strip())
ans = []
for i in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    ans.append(result)
    
for i in ans:
    print(i)