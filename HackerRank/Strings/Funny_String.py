#!/bin/python3

#https://www.hackerrank.com/challenges/funny-string/problem

import sys

def funnyString(s):
    length = len(s)
    flag = 0
    for i in range(1, length):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[length - 1 - i]) - ord(s[length - 1 - (i - 1)])):
            flag = 1
            break
    if flag == 1:
        return "Not Funny"
    elif flag == 0:
        return "Funny"

q = int(input().strip())
for i in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)