// Write a algorithm/function to delete an element from an array at a specified position. 

# include <stdio.h>

void displaydata(int arr[], int size){
    for (int i = 0; i<size; i++){
        printf("%d ", arr[i]);
    }
}

int deletedata(int arr[], int size, int index){

    for (int i= index; i< size; i++){
        arr[i]=arr[i+1];
    }
    return 1;
}

int main()
{
    int arr[10]= {1,23,4,56,6};
    int size= 5, index = 3;
    
    displaydata(arr, size);
    deletedata(arr, size, index);
    size= 4;
    displaydata(arr, size);

    return 0;
}
