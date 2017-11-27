#https://www.hackerrank.com/challenges/chocolate-feast/problem

import sys

def totalChocolates(n, c, m):
    count = n//c
    total = count
    
    rem = 0
    while rem + count >= m:
        prev_rem = rem
        rem = (prev_rem + count) % m
        count = (prev_rem + count) // m
        total += count

    return total

t = int(input().strip())
answer = []
for i in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    ans = totalChocolates(n, c, m)
    answer.append(ans)

    
for i in answer:
    print(i)