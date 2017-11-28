#!/bin/python3

#https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

def maximumSum(arr, size, mod_value):
    sums = [-1] * size
    temp = [-1] * 2
    temp[0] = arr[0] % mod_value
    temp[1] = 0
    sums[0] = temp
    for position in range(1, size):
        temp = [-1] * 2
        temp[0] = (sums[position-1][0] + (arr[position] % mod_value)) % mod_value
        temp[1] = position
        sums[position] = temp

    sums = sorted(sums)
    minimum = -1

    for position in range(0, size-1): 
        if sums[position][1] > sums[position + 1][1] and (sums[position + 1][0] - sums[position][0] < minimum or minimum == -1):
            minimum = sums[position + 1][0] - sums[position][0]

    if sums[size-1][0] > mod_value - minimum: 
        minimum = mod_value - sums[size-1][0]
        
    return mod_value - minimum

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        a = list(map(int, input().strip().split(' ')))
        result = maximumSum(a, n, m)
        print(result)