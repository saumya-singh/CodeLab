#!/bin/python3

#https://www.hackerrank.com/challenges/minimum-distances/problem

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

dictionary = {}
min_dis = n

for i in range(n):
    try:
        min_dis = min(i - dictionary[A[i]], min_dis)
    
    except:
        dictionary[A[i]] = i
        
if min_dis == n:
    print(-1)
else:
    print(min_dis)