#!/bin/python3

#https://www.hackerrank.com/challenges/reduced-string/problem

import sys

def super_reduced_string(s):
    str_list = []
    for m in s:
        str_list.append(m)
    i = 1
    while i < len(str_list):
        if str_list[i] == str_list[i - 1]:
            str_list.pop(i - 1)
            str_list.pop(i - 1)
            if i > 1:
                i -= 1
        else:
            i += 1
          
    if len(str_list) == 0:
        return "Empty String"
    else:
        string = ""
        for i in str_list:
            string = string + i
        return string
            
s = input().strip()
result = super_reduced_string(s)
print(result)