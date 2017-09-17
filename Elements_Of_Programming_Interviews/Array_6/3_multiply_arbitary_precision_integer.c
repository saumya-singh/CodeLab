#include<stdio.h>

int * reverseArray(int array[], int count){

	int counter, temp;

	for (counter = 0; counter < (count/2); counter++){
		temp = array[counter];
		array[counter] = array[count - counter - 1];
		array[count - counter - 1] = temp;
	}

	return array;
}

int main(){
	
int count1, count2, counter, i, j;
int *rev_array1, *rev_array2;

	printf("enter the number of digits in the first number:");
	scanf("%d", &count1);
	printf("\n");

	printf("enter the number of digits in the second number:");
	scanf("%d", &count2);
	printf("\n");

	int array1[count1], array2[count2], result[count1 + count2];

	printf("enter the digits of the first number");
	for(counter = 0; counter < count1; counter++){
		scanf("%d",&array1[counter]);
	}

	printf("enter the digits of the second number");
	for(counter = 0; counter < count2; counter++){
		scanf("%d",&array2[counter]);
	}

	//reversing the digits

	rev_array1 = reverseArray(array1, count1);
	rev_array2 = reverseArray(array2, count2);

	// making entries of result array zero

	for(i = 0; i < count1 + count2; i++){
		result[i] = 0;
	}

	//multiplication

	for(i = 0; i < count2; i++){
		for(j = 0; j < count1; j++){

			result[i +j] = result[i+j] + ((*(rev_array1 + j)) * (*(rev_array2 + i)));
			result[i + j +1] += result[i + j]/10;
			result[i + j] = result[i+j] % 10;
		}
	}

	printf("\nThe result is (multiplication):");
	for(i = count1 + count2 - 1; i >= 0 ; i--){
		printf("%d\n", result[i]);
	}

	return 0;
}

