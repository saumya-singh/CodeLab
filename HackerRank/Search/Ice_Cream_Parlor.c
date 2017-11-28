//https://www.hackerrank.com/challenges/icecream-parlor/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int i, j, t, k, m, n, cost[10000],cost_copy[10000], hash[10000], result[50][2], diff, first, last, temp, var1, var2;
    scanf("%d", &t);
    //printf("\n");
    for(i = 0; i < t; i++){
        scanf("%d", &m);
        //printf("\n");
        scanf("%d", &n);
        //printf("\n");
        for(k = 0; k < n; k++){
            scanf("%d", &cost[k]);
            cost_copy[k] = cost[k];
        }
        
        for (k = 0; k < n-1; k++){   
            for (j = 0; j < n-k-1; j++) {
                if (cost[j] > cost[j+1]){
                    temp = cost[j];
                    cost[j] = cost[j + 1];
                    cost[j + 1] = temp;
                }
            }
        }
        
        first = 0;
        last = n - 1;
        
        while(first < last){
            
            if( cost[first] + cost[last] == m){
                
                for(k = 0; k < n; k++){
                    if((cost_copy[k]== cost[first]) || (cost_copy[k]== cost[last])){
                        var1 = k;
                        break;
                    }  
                }
                
                for(k = var1; k < n; k++){
                    if((cost_copy[k]== cost[first]) || (cost_copy[k]== cost[last])){
                         var2 = k;
                    }  
                }
                
                result[i][0] = var1 + 1;
                result[i][1] = var2 + 1;
                break;
            }
            
            else if(cost[first] + cost[last] < m){
                first++;
                continue;
            }
            
            else if(cost[first] + cost[last] > m){
                last--;
                continue;
            }
        }
    }
    
    for(i = 0; i < t; i++){
            printf("%d %d", result[i][0], result[i][1]);
        printf("\n");
    }
    return 0;
}
