#include<stdio.h>

unsigned multiply( unsigned x, unsigned y);
unsigned add( unsigned num_1, unsigned num_2);

int main(){
	
	unsigned number_1, number_2;
	unsigned answer;
	
	printf("Enter the two numbers to be multiplied:");
	scanf("%u %u", &number_1, &number_2);
		
	answer = multiply(number_1, number_2);
	
	printf("\nThe answer is: %u", answer);
	return 0;
}

unsigned multiply( unsigned x, unsigned y){

	unsigned sum = 0, i=0;

	while( x ){
	
		if (x & 1){
			sum = add( sum , y);
		}
		i++;
		x = x >> 1;
		y = y << 1;
	}
	return sum;
}

unsigned add( unsigned num_1, unsigned num_2){
	
	unsigned carryin = 0, sum = 0, carryout, mask = 1, a, b, a_mask, b_mask, i = 0;
	
	a = num_1;
	b = num_2;
	
	while ( a||b ){
	
		a_mask = a & mask;
		b_mask = b & mask;
	
		sum = sum | ((a_mask ^ b_mask ^ carryin) << i);
		i++;
		
		if ((a_mask & b_mask) | (a_mask & carryin) | (b_mask & carryin)){
			carryout = 1;
		}
		
		else
			carryout = 0;
			
		a >>= 1;
		b >>= 1;
		carryin = carryout;
	}
	
	if (carryin == 1){
		sum = sum | (carryin << i);
	}
	
	return sum;	
}
