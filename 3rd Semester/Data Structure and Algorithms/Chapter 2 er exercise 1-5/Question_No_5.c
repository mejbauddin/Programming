// 5: Write a algorithm/function that finds and returns the maximum element in an array.
#include <stdio.h>

int findMax(int arr[], int size){
    int Max = arr[0];
    for (int i = 0; i < size; i++)
    {
        if(Max < arr[i]){
            Max = arr[i];
        }
    }
    printf("Maximum Element : %d ", Max);
    
}
int main(){
    int arr[10]={1,3,4,5,7};
    int size = 5;
    findMax(arr, size);
}