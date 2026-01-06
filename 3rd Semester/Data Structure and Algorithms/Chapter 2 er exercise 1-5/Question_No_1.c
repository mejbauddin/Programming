// 1: Write a algorithm/function to initialize an array of size 10 with the first 10 positive integers.

#include <stdio.h>

void displaydata(int arr[], int size){

	for (int i = 0; i<size; i++){
    	printf("%d ", arr[i]);
    }
    printf("\n");

}

int main(){

    int arr[10];

    for (int i = 0; i<10; i++){
        arr[i] = i+1;
    }

    displaydata(arr, 10);
    return 0;
}