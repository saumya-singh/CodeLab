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
struct node * mergeLists(struct node * head1, struct node * head2);

int main(){

	int list1, list2;

	// first list

	head1 = NULL;

	printf("enter the number of elements in the first list: ");
	scanf("%d", &list1);
	head1 = createList(list1, head1);
	printf("\nThe list is: ");
	print(head1);
	printf("\n");

	//second list

	head2 = NULL;

	printf("\n\nenter the number of elements in the second list: ");
	scanf("%d", &list2);
	head2 = createList(list2, head2);
	printf("\nThe list is: ");
	print(head2);
	printf("\n");

	//merging of the lists

	head1 = mergeLists(head1, head2);
	printf("\nThe merged list is: ");
	print(head1);

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

struct node * mergeLists(struct node * head1, struct node * head2){

	struct node * head;
	struct node * temp;

	if((head1 -> data) <= (head2 -> data)){
		head = head1;
		temp = head1;
		head1 = head1 -> next;
	}

	else{
		head = head2;
		temp = head2;
		head2 = head2 -> next;
	}

	while (head1 != NULL && head2 != NULL){


		if((head1 -> data) <= (head2 -> data)){

			temp -> next = head1;
			temp = head1;
			head1 = head1 -> next;
		}

		else{

			temp -> next = head2;
			temp = head2;
			head2 = head2 -> next;
		}
	}

	if(head1 != NULL)
		temp -> next = head1;
	else if(head2 != NULL)
		temp -> next = head2;

	return head;
}

