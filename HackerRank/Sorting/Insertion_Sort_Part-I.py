#!/bin/python3

#https://www.hackerrank.com/challenges/insertionsort1/problem

def lastInsertion(n, array):
    element = array[n - 1]
    
    for i in range(n - 2, -1, -1):
        if element < array[i]:
            array[i + 1] = array[i]
            print(*array)
        else:
            array[i + 1] = element
            print(*array)
            break
        
    if i == 0 and element < array[i]:
        array[0] = element
        print(*array)
       
    return

n = int(input().strip())
array = list(map(int, input().strip().split(" ")))

lastInsertion(n, array)