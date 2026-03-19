#include<iostream>
using namespace std;

int main(){
    // Assignment Operator 
    int a = 10 ;
    int b = 5;
    a -= 5;
    a += 10;

    // Comparison Operators
    cout<<(a==b)<<endl;
    cout<<(a<=b)<<endl;
    cout<<(a>=b)<<endl;
    cout<<(a>b)<<endl;
    cout<<(a<b)<<endl;
    cout<<(a!=b)<<endl;

    // Logical Operator
    cout<<(a && b)<<endl;
    cout<<(a || b)<<endl;
    cout<<!(a && b)<<endl;
    



}