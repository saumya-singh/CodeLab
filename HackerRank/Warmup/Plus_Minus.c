//https://www.hackerrank.com/challenges/plus-minus/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    int count_negative = 0, count_positive = 0, count_zero = 0;
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
       if (arr[arr_i] < 0){
           count_negative++;
       }
       else if (arr[arr_i] == 0){
           count_zero++;
       }
       else if (arr[arr_i] > 0){
           count_positive++;
       }
       
    }
    
    printf("%f\n%f\n%f", (float)count_positive/n, (float)count_negative/n, (float)count_zero/n);
    
    return 0;
}
