#!/bin/python3

#https://www.hackerrank.com/challenges/string-construction/problemS

import sys

def stringConstruction(s):
    set_ele = {i for i in s}
    return len(set_ele)
    
    
if __name__ == "__main__":
    q = int(input().strip())
    ans = []
    for i in range(q):
        s = input().strip()
        result = stringConstruction(s)
        ans.append(result)
        
for i in ans:
    print(i)