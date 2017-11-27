#https://www.hackerrank.com/challenges/equality-in-a-array/problem

import sys

def equalise(n, arr):
    dictionary = {}
    for element in arr:
        value = dictionary.get(element, "None")
        if value == "None":
            dictionary[element] = 1
        else:
            dictionary[element] = int(value) + 1
            
    list_d = list(dictionary.items())
    
    count = 0
    max_ = 0
    for i in range(len(list_d)):
        count += list_d[i][1]
        if max_ < list_d[i][1]:
            max_ = list_d[i][1]
        
    return count - max_

n = int(input().strip())
arr = list(map(int, input().strip().split()))
min_ele = equalise(n, arr)
print(min_ele)