#!/bin/python3

#https://www.hackerrank.com/challenges/electronics-shop/problem

import sys

def getMoneySpent(keyboards, drives, n, m, s):
    keyboards.sort(reverse=True)
    drives.sort()
    ms = -1
    i = j = 0
    while i < n:
        while j < m:
            if keyboards[i]+drives[j] > s:
                break
            if keyboards[i]+drives[j] > ms:
                ms = keyboards[i]+drives[j]
            j += 1
        i += 1
    return ms

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

spenditure = getMoneySpent(keyboards, drives, n, m, s)
print(spenditure)