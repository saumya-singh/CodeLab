#!/bin/python3

#https://www.hackerrank.com/challenges/migratory-birds/problem

import sys

def migratoryBirds(n, arr):
    dictionary = {}
    for element in arr:
        value = dictionary.get(element, "None")
        if value == "None":
            dictionary[element] = 1
        else:
            dictionary[element] = int(value) + 1
            
    list_d = list(dictionary.items())
    
    max_ = list_d[0][1]
    index = list_d[0][0]
    for i in range(len(list_d)):
        if max_ < list_d[i][1]:
            max_ = list_d[i][1]
            index = list_d[i][0]
    
    return index

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)