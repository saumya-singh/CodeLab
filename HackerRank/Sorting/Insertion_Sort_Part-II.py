#!/bin/python3

#https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort(unsort_list):
    length = len(unsort_list)
    for i in range(1, length):
        #print(unsort_list)
        element = unsort_list[i]
        for j in range(i - 1, -1, -1):
            if element < unsort_list[j]:
                unsort_list[j + 1] = unsort_list[j]
                if j == 0:
                    unsort_list[0] = element
            elif element >= unsort_list[j]:
                unsort_list[j + 1] = element
                break
        print(*unsort_list)
    return


n = int(input().strip())
unsort = [int(i) for i in input().strip().split()]
insertionSort(unsort)