//4: Write a algorithm/function to search for the first occurrence of an element in an array and return its position.

# include <stdio.h>

int main(){
    int arr[10]= {23,35,25,63,34};
    int key=25, size=5;

    for (int i = 0; i<size; i++){
        if(arr[i] == key){
            printf("element in an array position : %d", i+1);
        }
    }
    
}