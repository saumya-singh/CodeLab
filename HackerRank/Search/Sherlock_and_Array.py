#!/bin/python3

#https://www.hackerrank.com/challenges/sherlock-and-array/problem

import sys

def solve(a):
    sum = 0
    
    if len(a) == 1:
        return "YES"
    
    for number in a:
        sum = sum + number
       
    sum_part1 = sum_part2 = 0
    for i in range(1, len(a) - 1):
        sum_part1 = sum_part1 + a[i -1]
        sum_part2 = sum - sum_part1 - a[i]
        if sum_part1 == sum_part2:
            return "YES"
    return "NO"
        

T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
