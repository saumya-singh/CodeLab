#include<stdio.h>

void testPrime(int is_prime[], int limit);

int main(){

	int limit, index, counter;

	printf("enter the number till which we have to determine whether it is prime or not: ");
	scanf("%d", &limit);
	printf("\n");

	index = ((limit - 3)/2) + 1;
	int prime_array[index];

	for(counter = 0; counter < index; counter++){
		prime_array[counter] = 1;
	}

	testPrime(prime_array, index);

	printf("\nthe prime numbers in the range are: \n%d\n", 2);
	for(counter = 0; counter < index; counter++){
		if(prime_array[counter] != 0){
			printf("%d\n", (2 * counter) + 3);
		}
	}
	return 0;
}

void testPrime(int is_prime[], int index){

	int counter_1, counter_2, number;

	for(counter_1 = 0; counter_1 < index; counter_1++){
		if(is_prime[counter_1] == 1){
			for(counter_2 = (2 * counter_1 * counter_1 + 6 * counter_1 + 3); counter_2 <= index; counter_2 = counter_2 + 2 * counter_1 + 3){
				is_prime[counter_2] = 0;
			}
		}
	}
	return;
}