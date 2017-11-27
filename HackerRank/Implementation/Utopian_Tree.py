#!/bin/python3

#https://www.hackerrank.com/challenges/utopian-tree/problem

import sys

answer = []
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    count = 0
    h = 1
    
    rem = n%2 
    
    while count < n - rem:
        h = h * 2
        h += 1
        count += 2
        
    if rem == 1:
        h *= 2
       
    answer.append(h)
        
for i in answer:
    print(i)