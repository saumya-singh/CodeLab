#include<stdio.h>

int main(){

	int x, i, y;
	
	i = 0;
	x = 101;
	y = x;
	while (y){
		if ((y & 0x00000003) == 1 || (y & 0x00000003) == 2){
			x = x ^ (0x00000003 << i);
			break;
		}
		
		y = y>>1;
		i++;
	}
	printf("\nNew number: %d\n", x);
	return 0;
}	

