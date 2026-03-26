#include <iostream>
using namespace std;

int main(){
 // Array 
    // one dimensional
int arr1[5];
arr1[0] = 10;
arr1[1] = 20;
arr1[2] = 30;
arr1[3] = 40;
arr1[4] = 50;

for(int i = 0; i < 5; i++){
    cout<<arr1[i]<<endl;
}

// Another way
int arr2[10] = {1,2,3,4,5,6,7,8,9,10};
for(int i = 0; i < 10; i++){
    cout<<arr2[i]<<endl;
}


// memory address 
cout<<arr2<<endl;
cout<<&arr2[0]<<endl;
cout<<&arr2[1]<<endl;

    // Two dimensional
int arr3[2][3];
arr3[0][0] = 10;
arr3[0][1] = 20;
arr3[0][2] = 30;
arr3[1][0]= 40;
arr3[1][1] = 50;
arr3[1][2] = 60;

int n = sizeof(arr3)/sizeof(arr3[0]);
cout<<n<<endl;
for(int i = 0; i < 5; i++){
    cout<<arr1[i]<<endl;
}

}