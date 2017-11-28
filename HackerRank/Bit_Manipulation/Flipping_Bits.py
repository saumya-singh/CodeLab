#!/bin/python3

#https://www.hackerrank.com/challenges/flipping-bits/problem

import sys

n = int(input().strip())
answer = []

for number in range(n):
    number = int(input().strip())
    ans = number ^ ( 2 ** 32 - 1 )
    answer.append(ans)
    
for number in answer:
    print(number)