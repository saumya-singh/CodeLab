#!/bin/python3

#https://www.hackerrank.com/challenges/bon-appetit/problem

import sys

def bonAppetit(n, k, b, ar):
    sum_items = 0
    for i in range(n):
        if i == k:
            continue
        sum_items += ar[i]
    actual_bill = sum_items//2
    
    if b == actual_bill:
        return "Bon Appetit"
    else:
        return b - actual_bill

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)