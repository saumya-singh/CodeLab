#!/bin/python3

#https://www.hackerrank.com/challenges/pangrams/problem

import sys

def pangram(s):
    
    alpha_set = set("abcdefghijklmnopqrstuvwxyz")
    length = len(s)
    for i in range(length):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            char = chr(ord(s[i]) + 32)
        else:
            char = s[i]
        alpha_set.discard(char)
        
    if len(alpha_set) == 0:
        return "pangram"
    else:
        return "not pangram"

s = input().strip()
ans = pangram(s)
print(ans)