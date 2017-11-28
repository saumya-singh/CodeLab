#!/bin/python3

#https://www.hackerrank.com/challenges/anagram/problem

import sys

def makingAnagrams(s1, s2):

    diff = 0
    
    dictionary1 = {}
    for i in s1:
        if dictionary1.get(i, "None") == "None":
            dictionary1[i] = 1
        else:
            dictionary1[i] += 1
            
    dictionary2 = {}
    for i in s2:
        if dictionary2.get(i, "None") == "None":
            dictionary2[i] = 1
        else:
            dictionary2[i] += 1

    for key1, value1 in dictionary1.items():
        if dictionary2.get(key1, "None") == "None":
            continue
        else:
            v = dictionary2.get(key1) - value1
            if v <= 0:
                val = 0
            else:
                val = v
            dictionary2[key1] = val
    
    
    for key2, value2 in dictionary2.items():
        diff += value2
        
    return diff


def anagram(s):
    length = len(s)
    if length % 2 == 1:
        return -1
    else:
        mid_value = length // 2
        str1 = s[ : mid_value]
        str2 = s[mid_value : ]
        
        diff = makingAnagrams(str1, str2)
        return diff
    
q = int(input().strip())
ans = []
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    ans.append(result)

for i in ans:
    print(i)