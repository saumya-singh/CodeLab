#https://www.hackerrank.com/challenges/kaprekar-numbers/problem

import sys

def kaprekarNumber(a, b):
    #print("entered")
    list1 = []
    for i in range(a, b+1):
        #print("i-----", i)
        digit_count = 0
        num = i
        while num != 0:
            digit_count  += 1
            num = num//10
         
        #print("digit_count", digit_count)
        square = i * i
        #print("square-------", square)
        #square_copy = square
        count = 0
        r = 0
        
        while (count < digit_count):
            digit = square % 10
            square = square // 10
            r = r + digit * (10 ** count)
            count += 1
            
        l = square
        
        #print("l-------", l)
        #print("r-------", r)
        if l + r == i:
            list1.append(i)
         
    return list1


if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    ans_list = kaprekarNumber(a, b)
    
    if len(ans_list)==0:
        print("INVALID RANGE")
        
    else:
        l = " ".join([str(i) for i in ans_list])
        print(l)