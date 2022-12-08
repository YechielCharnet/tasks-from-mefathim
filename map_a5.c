#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};


void insert(struct Node** head_ref, int new_data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = new_data;
	new_node->next = (*head_ref);
	(*head_ref) = new_node;
}

static void reverse(struct Node** head_ref){
    struct Node* prev = NULL;
    struct Node* current = *head_ref;
    struct Node* next = NULL;
    while (current != NULL) {
    	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
    }
    *head_ref = prev;
}

void printList(struct Node* head){
	struct Node* temp = head;
	while (temp != NULL){
		printf("%d\n", temp->data);
		temp = temp->next;
	}
}


int main(){
	struct Node* head = NULL;

	insert(&head, 20);
	insert(&head, 4);
	insert(&head, 15);
	insert(&head, 85);

	printf("The linked lst is:\n");
	printList(head);

	reverse(&head);
	printf("\nReversed linked list \n");
	printList(head);
}



