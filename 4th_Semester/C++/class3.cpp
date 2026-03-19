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
    
    // Conditional Statements
    int X;
    cin >> X; // Get input from user
    cout<< "Enter your Score : "<<endl;
    if (X >= 90){
        cout<<"Very Good"<<endl;
    }else if (X >= 80){
        cout<<"Good"<<endl;
    }else if (X <=70){
        cout<<"ok"<<endl;
    }else if (X <=60){
        cout<<"Pass"<<endl;
    }else if (X < 60){
        cout<<"Fail"<<endl;
    }


}