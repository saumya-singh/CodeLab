#!/bin/python3

#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def energyLeft(n, k, c):
    E = 100
    i = (0 + k) % n
    while i != 0:
        if c[i] == 0:
            E -= 1
        elif c[i] == 1:
            E -= 3
        i = (i + k) % n 
    
    if i == 0:
        if c[i] == 0:
            E -= 1
        elif c[i] == 1:
            E -= 3
    
    return E

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
result = energyLeft(n, k, c)
print(result)