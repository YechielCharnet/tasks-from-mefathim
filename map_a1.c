#include <stdio.h>
#define ARRAT_SIZE 10

void insertionSort(int Array[]);

int main(){
	int Array[ARRAT_SIZE];
	for (int i = 0; i < ARRAT_SIZE; i++){
		printf("Enter %d a element: ",i);
		scanf("%d",&Array[i]);
	}
	for (int i = 0; i < ARRAT_SIZE; i++){
		printf("%d", Array[i]);
		printf(",");
	}
	printf("\n");
	
	insertionSort(Array);
	for (int i = 0; i < ARRAT_SIZE; i++){
		printf("%d", Array[i]);
		printf(",");
	}
	printf("\n");
	return 0;
}

void insertionSort(int Array[]){
	int i, key, j;
	for (i = 1; i < ARRAT_SIZE; i++){
		key = Array[i];
		j = i-1;
		while (j >= 0 && Array[j] < key){
			Array[j+1] = Array[j];
			j = j-1;
		}
		Array[j+1] = key;
	}
}
