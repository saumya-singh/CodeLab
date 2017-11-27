#!/bin/python3

#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def reverse(l):
    power = 0
    num = 0
    x = l
    while x > 0:
        rem = x%10
        num = num * 10 + rem 
        x = x // 10
        power += 1
    return num


i, j, k = map(int, input().strip().split())

count = 0
for l in range(i, j + 1):
    reverse_num = reverse(l)
    if (abs(l - reverse_num)) % k == 0:
        count += 1
print(count)