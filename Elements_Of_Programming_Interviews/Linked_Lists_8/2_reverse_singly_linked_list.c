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
struct Node * reverse();

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

	// reverse the list

	head = reverse();
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

struct Node * reverse(){

	struct Node * previous;
	struct Node * current;
	struct Node * next;

	previous = NULL;
	current = head;
	head = tail;
	tail = current;

	while(current != NULL){
		next = current -> next;
		current -> next = previous;
		previous = current;
		current = next;
	}

	return head;
}
