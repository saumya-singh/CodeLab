#!/bin/python3

#https://www.hackerrank.com/challenges/gem-stones/problem

import sys

def gemstones(arr):
    flag = 0
    length = len(arr)
    set_ele = set()
    element_set = {element for element in arr[0]}
    for elements in element_set:
        for i in range(1, length):
            if elements in arr[i]:
                set_ele.add(elements)
            else:
                set_ele.discard(elements)
                break
    return len(set_ele)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)