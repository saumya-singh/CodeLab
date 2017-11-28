#!/bin/python3

#https://www.hackerrank.com/challenges/missing-numbers/problem

import sys

n = int(input().strip())
A = list(map(int, input().strip().split(' ')))

m = int(input().strip())
B = list(map(int, input().strip().split(' ')))

for element in A:
    if element in B:
        B.remove(element)
        
setA = set()
setA.update(B)
setA = list(setA)
setA.sort()

for element in setA:
    print(element, end=" ")