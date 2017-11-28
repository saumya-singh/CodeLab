//https://www.hackerrank.com/challenges/time-conversion/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* timeConversion(char* s) {
    // Complete this function
    int hours;
    
    int h1 = s[0] - '0';
    int h2 = s[1] - '0';
    
    hours = h1 * 10 + h2;
    
    if((s[8] == 'p' && hours != 12) || (s[8] == 'P' && hours != 12)){
        hours = 12 + hours;  
    }
    
    else if((s[8] == 'a' && hours == 12) || (s[8] == 'A' && hours == 12)){
        hours = 0;
    }
    
    int var = hours/10;
    s[0] = (char)(var + '0');
    s[1] = (char)(hours%10 + '0');
    
    s[8] = '\0';
    return s;    
    
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
        int result_size;
    char* result = timeConversion(s);
    printf("%s\n", result);
    return 0;
}
