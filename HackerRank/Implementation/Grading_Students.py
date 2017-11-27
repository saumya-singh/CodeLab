#!/bin/python3
#https://www.hackerrank.com/challenges/grading/problem

import sys

def solve(grades):
    
    for index, marks in enumerate(grades):
        quotient = marks//5
        diff = ((quotient + 1) * 5) - marks
        if marks > 37 and diff < 3:
            marks = (quotient + 1) * 5 
            grades[index] = marks
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

