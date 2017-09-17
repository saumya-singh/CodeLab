# include<stdio.h>

void selectionSort(int array[], int numberOfElements){
	int i, j, temp;
	for (i=0 ; i<numberOfElements-1 ; i++){
		int min = i;
		for (j=i+1 ; j<numberOfElements ; j++){
			if (array[min] > array[j])
				min = j;
			}
		temp = array[i];
		array[i] = array[min];
		array[min] = temp;
		}
		
	printf("Sorted Array: \n");	
	for(i=0;i<numberOfElements;i++){
		printf(" %d ",array[i]);
		printf("\n");
		}
}

