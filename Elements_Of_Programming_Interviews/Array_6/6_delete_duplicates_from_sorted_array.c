#include<stdio.h>

int main(){

	int i , array[20], numberOfElements, m;
	int counter, digit, j, min, k;
	
	printf("enter the no. of elements:");
	scanf("%d", &numberOfElements);
	
	printf("\nenter the key:");
	scanf("%d", &m);
	
	printf("\nenter the array:");
	for ( i = 0 ; i < numberOfElements ; i++){
		scanf ("%d", &array[i]);
	}
	
	if (m < 2)
		min = m;
	else
		min = 2;
	
	counter = 1;
	digit = array[0];
	i = 1;
	j = i-2;
	
	while (i <= numberOfElements){
		if ( array[i] == digit){
			counter++;
			i++;
		}
		
		else {
			if ( counter == m ){
				for (k = 0 ; k < min ; k++){	
					j++;
					array[j] = digit;
				}
			}
				
			else {
				for (k = 0 ; k < counter ; k++){
					j++;
					array[j] = digit;
				}
			}
		
		if (i >= numberOfElements)
			break;		
		counter = 1;
		digit = array[i];
		i++;
				
		}
	
	} 	
	
	for ( i = 0 ; i < numberOfElements ; i++){
		printf ("\narray: ");
		printf ("%d  ", array[i]);
	}
	
}
