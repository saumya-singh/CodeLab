#include<stdio.h>

void insertionSort(int array[], int numberOfElements){
	int i,j;
	for (i=1 ; i<numberOfElements ; i++){
		int index = array[i];
		for (j = i-1 ; j>=0 && (index < array[j]) ; j--)
			array[j+1] = array[j];
		array[j+1] = index;
	}
	
	printf("Sorted Array: \n");	
	for(i=0 ; i<numberOfElements ; i++){
		printf(" %d ", array[i]);
		printf("\n");
	}
}
