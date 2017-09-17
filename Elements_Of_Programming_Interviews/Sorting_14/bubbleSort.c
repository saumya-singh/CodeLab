#include<stdio.h>

void bubbleSort(int array[], int numberOfElements){
	int i, j, temp;
	for (i = numberOfElements - 1 ; i > 0 ; i--){
		for (j=0 ; j<i ; j++){
			if (array[j] > array[j+1]){
			temp = array[j];
			array[j] = array[j+1];
			array[j+1] = temp;
			}
		}
	}
	printf("Sorted Array: \n");	
	for(i =  0 ; i < numberOfElements ; i++){
		printf(" %d ", array[i]);
		printf("\n");
	}

}
