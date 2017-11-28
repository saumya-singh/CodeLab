#!/bin/python3

#https://www.hackerrank.com/challenges/counter-game/problem

import sys

t = int(input().strip())
answer = []
for i in range(t):
    count = 0
    N = int(input().strip())
    
    while(N != 1):
        if N % 2 == 0:
            N = N/2
            count += 1
    
        else:
            i = 0
            while(2 ** i < N):
                i += 1
            power = i - 1
            N = N - (2 ** power)
            count += 1
            
    if count % 2 == 0:
        answer.append("Richard")
    else:
        answer.append("Louise")
    
for i in answer:
    print(i)
    