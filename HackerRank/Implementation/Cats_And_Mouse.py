#!/bin/python3

#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

import sys

def winner(x, y, z):
    if abs(x - z) > abs(y - z):
        return "Cat B"
    elif abs(y - z) > abs(x - z):
        return "Cat A"
    elif abs(y - z) == abs(x - z):
        return "Mouse C"

q = int(input().strip())
answer = []
for i in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    result = winner(x, y, z)
    answer.append(result)
    
for i in answer:
    print(i)