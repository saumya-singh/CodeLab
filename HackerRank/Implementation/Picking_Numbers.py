#!/bin/python3

#https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(n, a):
    dictionary = {}
    for element in a:
        value = dictionary.get(element, "None")
        if value == "None":
            dictionary[element] = 1
        else:
            dictionary[element] = int(value) + 1
            
    list_d = list(dictionary.items())
    list_d.sort()
    #print(list_d)
    
    if len(list_d) == 1:
          return list_d[0][1]
    
    max = 0
    for i in range(len(list_d)):
        if max < list_d[i][1]:
            max = list_d[i][1]
        
    for i in range(len(list_d) - 1):
        if abs(list_d[i][0] - list_d[i + 1][0]) == 1:
            add_result = list_d[i][1] + list_d[i + 1][1]
            if max < add_result:
                max = add_result
                
    return max
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = pickingNumbers(n, a)
print(count)