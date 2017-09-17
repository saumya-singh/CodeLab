#include<stdio.h>

int main(){

	int numberOfElements, counter, count_zero, count_two, temp;
	//int array[numberOfElements];

	printf("enter the no of elements in the array: \n");
	scanf("%d", &numberOfElements);

	int array[numberOfElements];

	printf("\nenter the array elements:\n");
	for(counter = 0; counter < numberOfElements; counter++){
		scanf("%d", &array[counter]);
	}

	count_zero = -1;
	count_two = numberOfElements;

	counter = 0;
	while(counter != count_two){
		if(array[counter] == 0){
			count_zero++;
			temp = array[count_zero];
			array[count_zero] = array[counter];
			array[counter] = temp;
			counter++;
		}

		else if(array[counter] == 1){
			counter++;
		}

		else if(array[counter] == 2){
			while(array[count_two - 1] == 2){
				count_two--;
			}
			count_two--;
			temp = array[count_two];
			array[count_two] = array[counter];
			array[counter] = temp;
			if (array[counter] == 1){
				counter++;
			}
		}
	}

	printf("\n the dutch national flag:");
	for(counter = 0; counter < numberOfElements; counter++){
		printf(" %d", array[counter]);
	}

	return 0;
}