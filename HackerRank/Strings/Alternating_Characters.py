#!/bin/python3

#https://www.hackerrank.com/challenges/alternating-characters/problem

import sys

def alternatingCharacters(s):
    string = []
    string.append(s[0])
    count = 1
    length = len(s)
    for i in range(1, length):
        if s[i] != string[count - 1]:
            string.append(s[i])
            count += 1
    st = ""
    for i in string:
        st += i
    return length - len(st)
        

q = int(input().strip())
answer = []
for i in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    answer.append(result)
    
for i in answer:
    print(i)
