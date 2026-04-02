// 题目：Complete number problem

// Description:
// Xiaoming is taking his final math exam and now he has encountered a question: If the sum of all factors of a positive integer greater than 1 is equal to itself, then the number is called a complete number. For example, 6 and 28 are both complete numbers: 6=1+2+3; 28=1+2+4+7+14. Please determine the number of perfect numbers between two positive integers. Xiaoming wants to ask the clever you to help him.

// Input format
// The input contains two positive integers n1 and n2, representing the data range in the question description.
// Positive integers are separated by spaces.
// Output format


#include <iostream>
using namespace std;

bool isPerfect(int num) {
    if (num <= 1) return false;
    int sum = 1;
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0)
            sum += i;
    }
    return sum == num;
}

int main() {
    int n1, n2;
    cin >> n1 >> n2;
    
    int count = 0;
    for (int i = n1; i <= n2; i++) {
        if (isPerfect(i)) {
            count++;
        }
    }
    
    cout << count;
    return 0;
}