#!/bin/python3

#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import sys

answer_list = []

string = "hackerrank"
q = int(input().strip())
for i in range(q):
    flag = 0
    s = input().strip()
    
    list_element = []
    for element in s:
        list_element.append(element)
        
    index_list = []
    for element in string:
        if element in list_element:
            index = list_element.index(element)
            index_list.append(index)
            
            
            for i in range(index + 1):
                list_element.pop(0)
                
        else:
            flag = 1
            break
      
        
    if flag == 0:
        answer_list.append("YES")
    elif flag == 1:
        answer_list.append("NO")

for element in answer_list:
    print(element)