#include<stdio.h>

int main(){
	
	int numberOfElements, counter, key, count;

	printf("enter the no. of elements in the array");
	scanf("%d", &numberOfElements);

	int array[numberOfElements];

	printf("enter the elements in the array:");
	for(counter = 0; counter < numberOfElements; counter++){
		scanf("%d", &array[counter]);
	}

	printf("enter the key of the array");
	scanf("%d", &key);

	count = 0;
	for(counter = 0; counter < numberOfElements; counter++){
		if(array[counter] != key){
			array[count++] = array[counter];
		}
	}

	printf("\nnew elements of the array:");
	for(counter = 0; counter < numberOfElements; counter++){
		printf("%d", array[counter]);
	}

	return 0;
}