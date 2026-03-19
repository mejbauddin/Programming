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

    // Switch Statement

    switch (X)
    {
    case 10:
        cout<<"This is your GPA : A"<<endl;
        break;
    case 9:
        cout<<"This is your GPA : B"<<endl;
        break;
    case 8:
        cout<<"This is your GPA : C"<<endl;
        break;
    case 7:
        cout<<"This is your GPA : D"<<endl;
        break;
    case 6:
        cout<<"This is your GPA : E"<<endl;
        break;
    
    default:
        cout<<"This is your GPA : F"<<endl;
        break;
    }


    // Loop
    int num = 0;
    while(num<=100){
        cout<< num<<endl;
        num++;
    }
}