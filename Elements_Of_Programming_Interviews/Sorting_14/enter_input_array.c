#include<stdio.h>

void quickSort(int array[], int start, int rear);

int main(){

	int counter, numberOfElements, initial;
	int inputArray[20];

	printf("Enter the no. of elements to be sorted\n");
	scanf("%d", &numberOfElements);
		
	printf("Enter the numbers to be sorted\n");
	
	for(counter=0 ; counter < numberOfElements ; counter++){
		scanf("%d", &inputArray[counter]);
		}

	//Sorting Algorithm
	initial = 0;
	quickSort(inputArray, initial, numberOfElements-1);
	
	printf("\nSorted array:\n");
	for (counter = 0; counter < numberOfElements ; counter++){
		printf("%d\n", inputArray[counter]);
	}
	return 0;	
}



