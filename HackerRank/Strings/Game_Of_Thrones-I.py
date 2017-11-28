#!/bin/python3

#https://www.hackerrank.com/challenges/game-of-thrones/problem

def gameOfThrones(s):
    dictionary = {}
    odd_count = 0
    for i in s:
        if dictionary.get(i, "None") == "None":
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    
    d_list = list(dictionary.items())
    length = len(d_list)
    for i in range(length):
        if d_list[i][1] % 2 == 1:
            odd_count += 1
    
    if odd_count == 0 or odd_count == 1:
        return "YES"
    else:
        return "NO"
          

s = input().strip()
result = gameOfThrones(s)
print(result)