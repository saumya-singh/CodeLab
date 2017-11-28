#!/bin/python3

#https://www.hackerrank.com/challenges/tutorial-intro/problem

def binarySearch(v, n, ar):
    first = 0
    last = len(ar)
    
    while first <= last:
        mid = (last + first)//2
        if v < ar[mid]:
            last = mid
        elif v > ar[mid]:
            first = mid + 1
        elif v == ar[mid]:
                return mid
          
    return -1
    


v = int(input().strip())
n = int(input().strip())
ar = [int(i) for i in input().strip().split(" ")]

index = binarySearch(v, n, ar)
print(index)