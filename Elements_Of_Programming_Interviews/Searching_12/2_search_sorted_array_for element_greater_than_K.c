#include<stdio.h>

int main(){

	int numberOfElements, lower_bound, upper_bound, mid, key, i;
	int array[20];

	printf("Enter the no. of elements in the array:");
	scanf("%d", &numberOfElements);

	printf("\nEnter the elements in the array:");
	for (i = 0; i < numberOfElements; i++)
	{
		scanf("%d", &array[i]);
	}

	printf("\nEnter the number to be found");
	scanf("%d", &key);

	lower_bound = 0;
	upper_bound = numberOfElements - 1;

	while ((upper_bound - lower_bound)  > 1){

		mid = lower_bound + (upper_bound - lower_bound)/2;

		if (array[mid] <= key){

			lower_bound = mid;
		}

		else if (array[mid] > key){

			upper_bound = mid;
		}
	}

	printf("\nThe index is:%d", lower_bound + 1);
	printf("\nThe element is:%d", array[lower_bound + 1]);

	return 0;
}