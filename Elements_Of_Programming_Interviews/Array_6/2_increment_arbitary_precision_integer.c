#include<stdio.h>
#include<stdlib.h>

int main(){

	int numberOfDigits, counter, pointer;
	int *array;
	//int array[numberOfDigits];

	printf("enter the number of digits");
	scanf("%d",&numberOfDigits);

	array = (int*) malloc(numberOfDigits * sizeof(int));

	printf("enter the number to be incremented");
	for(counter = 0; counter < numberOfDigits; counter++){
		scanf("%d",&array[counter]);
	}

	printf("\n----------------------------");

	pointer = numberOfDigits - 1;

	while(pointer >= 0){

		if(array[pointer] == 9){
			array[pointer] = 0;
			pointer--;
			continue;
		}

		else {
			array[pointer] = array[pointer] + 1;
			break;
		}
	}

	if((array[0] == 0) && pointer < 0){
		numberOfDigits = numberOfDigits + 1;
		array = (int*) realloc(array, (numberOfDigits) * sizeof(int));
		array[0] = 1;
		for(counter = 1; counter < numberOfDigits; counter++)
			array[counter] = 0;
	}

	for(counter = 0; counter < numberOfDigits; counter++){
		printf("%d", array[counter]);
	}
	return 0;
}