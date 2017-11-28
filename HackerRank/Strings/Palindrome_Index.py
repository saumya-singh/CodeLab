#!/bin/python3

#https://www.hackerrank.com/challenges/palindrome-index/problem

import sys

def palindromeIndex(s):
    length = len(s)
    counter = length//2
    i = 0
    j = length -1
    flag = 0
    while i < counter:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if s[i] == s[j - 1] and s[i + 1] == s[j - 2]:
                index = j
            elif s[j] == s[i + 1] and s[j - 1] == s[i + 2]:
                index = i
            flag = 1
            break
    if flag == 0:
        index = -1
    return index    

q = int(input().strip())
answer = []
for i in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    answer.append(result)
    
for i in answer:
    print(i)