#include<stdio.h>

int swapBits(int x , int i , int j);

int main(){
	
	int x, y, index_1, index_2;
	
	printf("Enter the number:");
	scanf("%d", &x);
	
	printf("\nEnter the indecies to be swaped:");
	scanf("%d %d", &index_1, &index_2);
	
	y = swapBits(x, index_1, index_2);
	
	printf("\nThe swapped number is:%d", y);
	return 0;
}

int swapBits(int x , int i , int j){
	
	if ( ((x >> i) & 1) != ((x >> j) & 1) ){
	
		x = x ^ ((1 << i) | (1  << j));
	}
	return x;
}
