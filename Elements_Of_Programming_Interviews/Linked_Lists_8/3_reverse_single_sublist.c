#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node * next;
};

struct Node * head;
struct Node * tail;

void reverseSection(int start, int finish);
void insert(int data);
void print();

int main(){

	int numberOfElements, counter, element, start, finish;

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

	printf("\nenter the sart and the end of the sublist: ");
	scanf("%d %d", &start, &finish);

	// reverse the section

	reverseSection(start, finish);

	printf("\nThe reversed list is: ");
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

void reverseSection(int start, int finish){

	int count = 1;
	struct Node * temp1;
	struct Node * temp2;
	struct Node * previous;
	struct Node * current;
	struct Node * next;

	previous = head;

	while(count < start - 1){

		previous = previous -> next;
		count++;
	}

	temp1 = previous;
	previous = previous -> next;
	temp2 = previous;
	current = previous -> next;
	count += 2;

	while(count <= finish){

		if(count == finish){
			temp1 -> next = current;
		}
		
		next = current -> next;
		current -> next = previous;
		previous = current;
		current = next;
		count++;
	}

	temp2 -> next = current;
	return;
}

