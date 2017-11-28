#!/bin/python3

#https://www.hackerrank.com/challenges/lonely-integer/problem

import sys

def lonelyinteger(a):
    
    list = []
    for i in range(101):
        list.append(0)
    
    for element in a:
        list[element] = list[element] ^ 1
        
    for index, element in enumerate(list):
        if element == 1:
            return index
            

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)