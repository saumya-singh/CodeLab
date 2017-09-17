#include<stdio.h>

int main(){

	int numberOfElements, counter, max;
	
	printf("enter the no. of elements in the array");
	scanf("%d", &numberOfElements);

	int array[numberOfElements];

	printf("enter the elements in the array:");
	for(counter = 0; counter < numberOfElements; counter++){
		scanf("%d", &array[counter]);
	}
	
	max = 0;

	for( counter = 0; counter <= max && max < numberOfElements; counter++){
		if (max < (counter + array[counter])){
			max = counter + array[counter];
		}
	}

	if (max >= numberOfElements - 1){
		printf("it reaches till the end");
	}
	else
		printf("it does not reaches till the end");

	return 0;
}