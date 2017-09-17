#include<stdio.h>

long double power( double x, int y);

int main(){
	
	double number_1
	int number_2;
	long double answer;
	
	printf("Enter the two numbers to be divided:");
	scanf("%lf %d", &number_1, &number_2);
		
	answer = divide(number_1, number_2);
	
	printf("\nThe answer is: %Lf", answer);
	return 0;
}

long double power( double x, int y){

	
}


