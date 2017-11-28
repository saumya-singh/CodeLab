//https://www.hackerrank.com/challenges/diagonal-difference/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n, i, diff; 
    int sum1 = 0, sum2 = 0;
    scanf("%d",&n);
    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          scanf("%d",&a[a_i][a_j]);
       }
    }
    
    for (i = 0; i < n; i++){
        sum1 = sum1 + a[i][i];
        sum2 = sum2 + a[i][n - 1 - i];
    }
    diff = abs(sum1 - sum2);
    printf("%d", diff);
    
    return 0;
}
