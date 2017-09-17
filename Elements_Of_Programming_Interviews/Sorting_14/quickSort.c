# include<stdio.h>

/*void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}*/

int partition(int array[], int start, int rear);

void quickSort(int array[], int start, int rear)
{	
	if (start < rear){
		int part = partition(array, start, rear);
		//printf("\n%d------%d\n", array[part], part);
		quickSort(array, start, part - 1);
		quickSort(array, part + 1, rear);
	}
}

int partition(int array[], int start, int rear){
	
	int pivot, i, j, temp;      // i and j are counters
	
	pivot = array[rear];
	i = start - 1;
	
	for(j = start ; j < rear ; j++){
			if (pivot > array[j]){
				++i;
				
				temp = array[j];
				array[j] = array[i];
				array[i] = temp;
			}
			
	}
	
	
	temp = array[rear];
	array[rear] = array[i + 1];
	array[i + 1] = temp;
	
	return i + 1;
}
