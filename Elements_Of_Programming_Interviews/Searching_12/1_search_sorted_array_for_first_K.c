#include<stdio.h>

int main(){

	int numberOfElements, lower_bound, upper_bound, mid, key, min_index, i;
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

	min_index = -1;
	lower_bound = 0;
	upper_bound = numberOfElements - 1;

	while (lower_bound <= upper_bound){

		mid = lower_bound + (upper_bound - lower_bound)/2;
		
		if (array[mid] == key){

			min_index = mid;
			upper_bound = mid - 1;
		}

		else if (array[mid] < key){

			lower_bound = mid + 1;
		}

		else {

			upper_bound = mid - 1;
		}
	}

	printf("\nThe index of the first occurence of the key is:%d", min_index);

	return 0;
}