//https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int birthdayCakeCandles(int n, int ar_size, int* ar) {
    // Complete this function
    int i, max = 0, count = 0;
    
    for(i = 0; i < n; i++){
        if(ar[max] < ar[i]){
            max = i;
            count = 0;
        } 
        
        if(ar[i] == ar[max]){
            count++;
        }
    }
    
    return count;
}

int main() {
    int n; 
    scanf("%i", &n);
    int *ar = malloc(sizeof(int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%i",&ar[ar_i]);
    }
    int result = birthdayCakeCandles(n, n, ar);
    printf("%d\n", result);
    return 0;
}