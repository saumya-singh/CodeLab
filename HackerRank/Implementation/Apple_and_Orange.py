#!/bin/python3

#https://www.hackerrank.com/challenges/apple-and-orange/problem

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

count_apple = 0
count_orange = 0

for distance in apple:
    if distance > 0:
        total = distance + a
        if total >= s and total <= t:
            count_apple += 1
            
for distance in orange:
    if distance < 0:
        total = b + distance
        if total >= s and total <= t:
            count_orange += 1
            
print(count_apple)
print(count_orange)