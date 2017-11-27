#!/bin/python3

#https://www.hackerrank.com/challenges/angry-professor/problem

import sys

answer=[]
t = int(input().strip())
for i in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    count = 0
    for time in a:
        if time <= 0:
            count+= 1
            
    if count < k:
        answer.append("YES")
    else:
        answer.append("NO")
        
for i in answer:
    print(i)