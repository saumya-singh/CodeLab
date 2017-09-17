#include<stdio.h>

int main(){

	int numberOfElements, i, min_element, j, max, max1, max2;
	int array[20];
	
	printf ("Enter the no. of elements");
	scanf("%d", &numberOfElements);
	
	printf("\nEnter the array");
	for( i = 0; i < numberOfElements; i++)
		scanf("%d", &array[i]);
		
	min_element = array[0];
	for ( i = 0; i < numberOfElements; i++){
		if ( min_element > array[i]){
			min_element = array[i];
		}
		
		array[i] = array[i] - min_element;
	}
	
	i = 0;
	j = 0;
	
	while (i < numberOfElements && j < numberOfElements){
		if (array[i] == 0)
			i++;
			
		max = array[i];
		while (array[i++] != 0 && i < numberOfElements){
			if (max < array[i])
				max = array[i];
		}
		
		array[j] = max;
		j++;
	}
	
	max1 = array[0];
	max2 = array[1];
	for ( i = 1; i < j; i++){
		if (array[i] > max1){
			max2 = max1;
			max1 = array[i];
		}
		
		else if (max1 > array[i] && max2 < array[i])
			max2 = array[i];
		
		else if (max1 == max2)
			max2 = array[i];
	}
	
	/*for ( i = 0; i < j; i++){
		printf("\narray:%d", array[i]);
	}*/
	
	printf("\nmaximum profit is: %d", max1 + max2);
	return 0;
}

