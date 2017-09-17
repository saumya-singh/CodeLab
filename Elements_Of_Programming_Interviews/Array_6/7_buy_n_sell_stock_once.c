#include<stdio.h>

int main(){

	int i, noOfElements, array[15], m_num, max_count, num, count;
	
	printf("Enter the no. of elements");
	scanf("%d", &noOfElements);
	
	printf("Enter the elements of the array");
	for( i = 0; i < noOfElements; i++){
		scanf("%d", &array[i]);
	}	
	
	max_count = 0;
	
	num = array[0];
	count = 1;
	
	for( i=1; i < noOfElements; i++){
		if ( array[i] != array[i-1]){
			if ( max_count < count){
				m_num = num;
				max_count = count;
			}
			
			num = array[i];
			count = 1;
		}
		
		else {
			count++;
		}
	}
	
	if ( max_count < count){
		m_num = num;
		max_count = count;
	}
	
	printf("number: %d\ncount: %d", m_num, max_count);
	return 0;
}
