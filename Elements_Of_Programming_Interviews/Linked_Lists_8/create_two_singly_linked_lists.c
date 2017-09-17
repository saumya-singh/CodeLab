#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node * next;
};

struct node * head1;
struct node * head2;

struct node * createList(int listSize, struct node * head);
void insert(int element, struct node ** pointerToHead);
void print(struct node * head);

int main(){

	int list1, list2;

	head1 = NULL;

	printf("enter the number of elements in the first list: ");
	scanf("%d", &list1);
	head1 = createList(list1, head1);
	printf("\nThe list is: ");
	print(head1);
	printf("\n");

	head2 = NULL;

	printf("\n\nenter the number of elements in the second list: ");
	scanf("%d", &list2);
	head2 = createList(list2, head2);
	printf("\nThe list is: ");
	print(head2);
	printf("\n");

	return 0;
}

struct node * createList(int listSize, struct node * head){

	int element, counter;

	for(counter = 0; counter < listSize; counter++){
		printf("\nenter the element: ");
		scanf("%d", &element);
		insert(element, &head);
	}

	return head;
}

void insert (int element, struct node ** pointerToHead){

	struct node* temp = (struct node*) malloc(sizeof(struct node));
	temp -> data = element;
	temp -> next = NULL;
	if( *pointerToHead == NULL ){
		*pointerToHead = temp;
		return;
	}

	struct node * temp1;
	temp1 = *pointerToHead;
	while ((temp1 -> next) != NULL){
		temp1 = temp1 -> next;
	}

	temp1 -> next = temp ;
	return;
}

void print(struct node* head){

	struct node * temp1;
	temp1 = head;
	while (temp1 != NULL){
		printf("%d ", temp1 -> data);
		temp1 = temp1 -> next;
	}
	return;
}
