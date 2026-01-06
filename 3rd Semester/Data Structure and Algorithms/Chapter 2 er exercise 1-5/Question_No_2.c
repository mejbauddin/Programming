// // Given an array and an element, write a algorithm/function to insert the element at a specified position.
// question 2
#include <stdio.h>

void displaydata(int arr[], int size){

	for (int i = 0; i<size; i++){
    	printf("%d ", arr[i]);
    }
    printf("\n");

}

int insertdata(int arr[], int size, int element, int index){
	
    for(int i = size-1; i >= index; i--){
    	arr[i+1] = arr[i];
    }
    arr[index]= element;
    return 1;
}

int main(){
	int arr[10]={1,2,3,4,5};
    int size = 5, element = 99, index = 3;
    displaydata(arr, size);
    insertdata(arr, size, element, index);
    size = size+1;
    displaydata(arr, size);


}

// question 3
