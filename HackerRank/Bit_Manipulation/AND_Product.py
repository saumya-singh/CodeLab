#!/bin/python3

#https://www.hackerrank.com/challenges/and-product/problem

import sys 

n = int(input().strip())
answer = []

for j in range(n):
    a, b = list(map(int, input().strip().split(' ')))
    
    power = 0
    ans = 0
    while(2 ** power <= a):
        power += 1
    
    if 2 ** (power - 1) == a and b < (2 ** (power)):
        answer.append(a)
        
    elif 2 ** (power - 1) < a and b < (2 ** (power)):
        pow = power - 1
       
        while (a >> pow) & 1 == (b >> pow) & 1:
            pow -= 1
        
        num = a
        for i in range(pow + 1):
            num = num & ~(1 << i)
            
        answer.append(num)
 
    else:
        answer.append(0)
        
for i in answer:
    print(i)
        
