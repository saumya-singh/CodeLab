#!/bin/python3

#https://www.hackerrank.com/challenges/countingsort1/problem

def count(n, ar):
    hash_table = []
    for i in range(100):
        hash_table.append(0)
    for number in ar:
        hash_table[number] += 1
    
    return hash_table

n = int(input().strip())
ar = [int(i) for i in input().strip().split(" ")]
hash_table = count(n, ar)
print(*hash_table)