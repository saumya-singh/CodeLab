#!/bin/python3

#https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

def makePalindrome(s):
	value = 0
	length = len(s)
	counter = length // 2
	for i in range(counter):

		if s[i] == s[length - 1 - i]:
			i += 1
		else:
			diff = abs(ord(s[length - 1 - i]) - ord(s[i]))
			value += diff

	return value


n = int(input().strip())
answer = []

for i in range(n):
	s = input().strip()

	cost = makePalindrome(s)
	answer.append(cost)

for i in answer:
	print(i)
