#!/bin/python3

#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import sys

def solve(year):
    
    normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    sum = 0
    month = 0 
    
    if year >= 1700 and year <= 1917:
        leap = year % 4
        if leap == 0:
            list = leap_year
        else:
            list = normal_year
        
            
    elif year >= 1918 and year <= 2700:
        
        if ((year % 4) == 0 and (year % 100) != 0) or year % 400 == 0 :
            list = leap_year
        else:
            list = normal_year
            
    for days in list:
        if sum <= 256:
            sum = sum + days
            month += 1
        else:
            break
    
    m1 = str(month//10)
    m2 = str(month%10)
    mm = m1 + m2
    
    day = 256 - (sum - list[month - 1]) 
    if year == 1918:
        day = day + 13
        
    dd = str(day)
    
    yyyy = str(year)
    
    return dd + '.' + mm + '.' + yyyy
    

year = int(input().strip())
result = solve(year)
print(result)