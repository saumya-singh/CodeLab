#!/bin/python3

#https://www.hackerrank.com/challenges/xor-se/problem

import sys

answer = []

def xor_sequence(limit):
    remainder = limit % 8
    if(remainder == 0 or remainder == 1):
        return limit
    if(remainder == 2 or remainder == 3):
        return 2
    if(remainder == 4 or remainder == 5):
        return limit + 2
    if(remainder == 6 or remainder == 7):
        return 0
    

Q = int(input().strip())
for i in range(Q):
    L,R = input().strip().split(' ')
    L,R = [int(L),int(R)]
    
    ans = xor_sequence(R) ^ xor_sequence(L - 1)
    answer.append(ans)
    
for element in answer:
    print(element)