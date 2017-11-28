#!/usr/bin/python3

#https://www.hackerrank.com/challenges/sansa-and-xor/problem

import sys

if __name__ == "__main__":
    answer = []
    T = int(input().strip())
    for i in range(T):
        n = int(input().strip())
        l = list(map(int, input().strip().split()))
        
        ans = 0
        if len(l)%2 == 0:
                ans = 0
        else:
            for i in range(0, len(l), 2):
                ans = ans ^ l[i]
                
        answer.append(ans)
    
    for i in answer:
        print(i)