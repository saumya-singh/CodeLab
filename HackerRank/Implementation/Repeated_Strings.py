#https://www.hackerrank.com/challenges/repeated-string/problem

import sys

def repeatedString(s, n):
    count = 0
    if n <= len(s):
        for index in range(n):
            if s[index] == 'a':
                count += 1
                
    else:
        sub_count = 0
        for index in range(len(s)):
            if s[index] == 'a':
                sub_count += 1
     
        times = n // len(s)
        rem = n - (times * len(s))
        count = sub_count * times
        for index in range(rem):
            if s[index] == 'a':
                count += 1

    return count
        
s = input().strip()
n = int(input().strip())

rep_count = repeatedString(s, n)
print(rep_count)