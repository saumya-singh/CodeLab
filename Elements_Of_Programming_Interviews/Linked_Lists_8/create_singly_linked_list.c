#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node * next;
};

struct Node * head;
struct Node * tail;

void insert(int data);
void print();

int main(){

	int numberOfElements, counter, element;

	head = NULL;
	tail = NULL;

	printf("enter the number of elements in the list: ");
	scanf("%d", &numberOfElements);

	for(counter = 1; counter <= numberOfElements; counter++){
		printf("\nenter the element: ");
		scanf("%d", &element);
		insert(element);
	}

	printf("\nThe list is: ");
	print();
	printf("\n");

	return 0;
}

void insert(int data){

	struct Node * temp;
	temp = (struct Node *)malloc(sizeof(struct Node));
	temp -> data = data;
	temp -> next = NULL;

	if(head == NULL){
		head = temp;
	}

	if(tail != NULL){
		tail -> next = temp;
	}
	tail = temp;
	return;
}

void print(){

	struct Node * temp;
	temp = head;
	while(temp != NULL){
		printf("%d ", temp -> data);
		temp = temp -> next;
	}
	return;
}