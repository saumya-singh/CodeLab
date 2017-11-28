#!/bin/python3

#https://www.hackerrank.com/challenges/runningtime/problem

def insertionSort(unsort_list):
    count = 0
    length = len(unsort_list)
    for i in range(1, length):
        element = unsort_list[i]
        for j in range(i - 1, -1, -1):
            if element < unsort_list[j]:
                unsort_list[j + 1] = unsort_list[j]
                count += 1
                if j == 0:
                    unsort_list[0] = element
            elif element >= unsort_list[j]:
                unsort_list[j + 1] = element
                break
    return count

n = int(input().strip())
unsort = [int(i) for i in input().strip().split()]

count = insertionSort(unsort)
print(count)