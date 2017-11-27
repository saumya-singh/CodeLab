#!/bin/python3

#https://www.hackerrank.com/challenges/circular-array-rotation/problem

import sys

def rotation(a, k):
    ans = []
    rot_factor = k % len(a)
    for i in range(len(a) - rot_factor, len(a)):
        ans.append(a[i])
        
    for i in range(len(a) - rot_factor):
        ans.append(a[i])
        
    return ans


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

rot_list = rotation(a, k)

answer = []
for i in range(q):
    m = int(input().strip())
    answer.append(rot_list[m])
    
for i in answer:
    print(i)