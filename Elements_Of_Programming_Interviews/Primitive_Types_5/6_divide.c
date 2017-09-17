#include<stdio.h>
#include<math.h>

int divide( int x, int y);
int power(int q_part);

int main(){
	
	int number_1, number_2;
	int answer;
	
	printf("Enter the two numbers to be divided:");
	scanf("%d %d", &number_1, &number_2);
		
	answer = divide(number_1, number_2);
	
	printf("\nThe answer is: %d", answer);
	return 0;
}

int divide( int x, int y){
	
	int k = 0;
	int q = 0, q_part;
	
	while ( x >= y ){
		if ( x >= (y << k)){
			k++;
		}
		
		else {
			q_part = k - 1;
			q = q + power(q_part);
			x = x - (y << q_part);
			k = 0;
		}
	}
	
	return q;	
}

int power(int q_part){
	
	int i, prod = 1;
	for ( i = 1 ; i <= q_part ; i++){
		prod = prod * 2;
	}
	return prod;	
}
