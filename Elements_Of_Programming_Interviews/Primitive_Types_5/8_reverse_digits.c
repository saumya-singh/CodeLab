#include<stdio.h>

int swapBits(unsigned int x , int i , int j);

int main(){
	
	unsigned int x;
	int i;
	int size = (sizeof(int) * 8);
	printf("size: %d\n", size); 
	
	printf("Enter the number:");
	scanf("%d", &x);
	
	for (i = 0 ; i < size/2 ; i++){
		x = swapBits(x, i, size - i - 1);
	}
	
	printf("\nThe reversed number is:%u", x);
	return 0;

}

int swapBits(unsigned int x , int i , int j){
	
	if ( ((x >> i) & 1) != ((x >> j) & 1) ){
	
		x = x ^ ((1 << i) | (1  << j));
	}
	
	return x;
}

