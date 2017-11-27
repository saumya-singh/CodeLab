#https://www.hackerrank.com/challenges/absolute-permutation/problem

def permutation(n, k):
    if k == 0:
        return (list(range(1, n+1)))
    elif (n/k) % 2 != 0:
        return ([-1])
    else:
        add = True
        perm = []
        
        for i in range(1, n+1):
            if add:
                perm.append(i+k)
                
            else:
                perm.append(i-k)
                
            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        return (perm)

t = int(input().strip())
answer = []
for i in range(t):
    n,k = map(int, input().split())
    result = permutation(n, k)
    answer.append(result)
for i in answer:
    print(*i)