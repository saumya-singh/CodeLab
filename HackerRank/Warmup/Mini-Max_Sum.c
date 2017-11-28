//https://www.hackerrank.com/challenges/mini-max-sum/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    
    int i, max = 0, min = 0;
    long int sum = 0, sum_max = 0, sum_min = 0;
    
    int *arr = malloc(sizeof(int) * 5);
    for(int arr_i = 0; arr_i < 5; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    
    for(i = 0; i < 5 ; i++){
        if(arr[max] < arr[i]){
            max = i;
        }
        if(arr[min] > arr[i]){
            min = i;
        }
        sum = sum + arr[i];
    }
    
    sum_max = sum - arr[min];
    sum_min = sum - arr[max];
    
    printf("%ld %ld", sum_min, sum_max);
    
    return 0;
}
