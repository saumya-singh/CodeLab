#!/usr/bin/python3

#https://www.hackerrank.com/challenges/maximizing-xor/problem

def maxXor(l, r):
    
    max = 0
    for x in (i for i in range(l, r + 1) if i % 2 == 0):
        for y in (j for j in range(l, r + 1) if j % 2 != 0):
            if (x ^ y) > max:
                max = x ^ y
             
    return max
  
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))