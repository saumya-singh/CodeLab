#!/bin/python3

#https://www.hackerrank.com/challenges/between-two-sets/problem

import sys

def getTotalX(a, b):
    x = max(a)
    y = min(b)
    count = 0
    for i in range(x, y + 1, x):
        flag = 0
        for ele1 in a:
            if i % ele1 != 0:
                flag = 1
                continue
        for ele2 in b:
            if ele2 % i != 0:
                flag = 1
                continue
        if flag == 0:
            count += 1
    return count
                

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)