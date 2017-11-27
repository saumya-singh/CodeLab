#!/bin/python3

#https://www.hackerrank.com/challenges/sock-merchant/problem

import sys

def sockMerchant(n, ar):
    dictionary = {}
    for element in ar:
        value = dictionary.get(element, "None")
        if value == "None":
            dictionary[element] = 1
        else:
            dictionary[element] = int(value) + 1
            
    list_d = list(dictionary.items())
    
    count = 0
    for i in range(len(list_d)):
        value = list_d[i][1]
        count += value // 2
    
    return count
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)