#!/bin/python3

#https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def rotate(n, s, k):
    k = k % 26
    string = ""
    for i in s:
        if (ord(i)>=65 and ord(i)<= (90 - k)) or (ord(i)>=97 and ord(i)<= (122 - k)):
            string += chr(ord(i) + k)
        elif (ord(i) > (90 - k) and ord(i) <= 90) or (ord(i) > (122 - k) and ord(i) <= 122):
            string += chr(ord(i) - (26 - k))
        else:
            string += i
    
    return string

n = int(input().strip())
s = input().strip()
k = int(input().strip())
string = rotate(n, s, k)
print(string)