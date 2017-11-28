#!/bin/python3

#https://www.hackerrank.com/challenges/making-anagrams/problem

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
            diff += value1
        else:
            diff += abs(value1 - dictionary2.get(key1))
            del dictionary2[key1]
    
    
    for key2, value2 in dictionary2.items():
        diff += value2
        
    return diff
    

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)

