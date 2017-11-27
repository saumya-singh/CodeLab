#!/bin/python3

#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import sys

def getRecord(s):
    max = min = s[0]
    high = low = 0
    length = len(s)
    for x in range(1, length):
        if max < s[x]:
            max = s[x]
            high = high + 1
        if min > s[x]:
            min = s[x]
            low = low + 1
     
    list = []
    list.append(high)
    list.append(low)
    
    return list
          
        
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))