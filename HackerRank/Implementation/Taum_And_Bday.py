#!/bin/python3

#https://www.hackerrank.com/challenges/taum-and-bday/problem

import sys

def minimumCost(b, w, x, y, z):
    if x <= y:
        cost = x * b
        if x + z <= y:
            cost += (x+z) * w
        else:
            cost += y * w
    else:
        cost = y * w
        if y + z <= x:
            cost += (y+z) * b
        else:
            cost += x * b
            
    return cost
        

t = int(input().strip())
answer = []
for i in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    cost = minimumCost(b, w, x, y, z)
    answer.append(cost)
    
for i in answer:
    print(i)
    
