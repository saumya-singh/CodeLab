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
int cyclicity();

int main(){

	int numberOfElements, counter, element, position;

	head = NULL;
	tail = NULL;

	printf("enter the number of elements in the list: ");
	scanf("%d", &numberOfElements);

	for(counter = 1; counter <= numberOfElements; counter++){
		printf("\nenter the element: ");
		scanf("%d", &element);
		insert(element);
	}

	struct Node * temp;
	temp = head -> next -> next;
	tail -> next = temp;

	/*printf("\nThe list is: ");
	print();
	printf("\n");*/

	// test for cyclicity

	position = cyclicity();

	if(position == 0){
		printf("\nno cycle");
	}

	else{
		printf("\nthe strting position of the cycle is: %d", numberOfElements - position + 1);
	}

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

int cyclicity(){

	int countCycle =1;

	struct Node * slow;
	struct Node * fast;

	fast = head;
	slow = head;

	printf("\nThe head is: %d", head -> data);

	while(fast && fast -> next && fast -> next -> next){

		slow = slow -> next;
		fast = fast -> next -> next;

		if(slow == fast){
			slow = slow -> next;

			while(slow != fast){
				slow = slow -> next;
				countCycle ++;
			}
		return countCycle;
		}
	}
	return 0;	
}