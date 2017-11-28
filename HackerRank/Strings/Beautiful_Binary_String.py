#!/bin/python3

#https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import sys

def minSteps(n, B):
    #string = ""
    count = 0
    i = 0
    while i <= n - 3:
        if B[i] == 0 and B[i + 1] == 1 and B[i + 2] == 0:
            B[i + 2] = 1
            count += 1
            #string += str(B[i]) + str(B[i + 1]) + str(B[i + 2])
            i += 3
        else:
            #string += str(B[i])
            i += 1
            continue
    
    return count

n = int(input().strip())
B = input().strip()
l = [int(i) for i in B]
result = minSteps(n, l)
print(result)