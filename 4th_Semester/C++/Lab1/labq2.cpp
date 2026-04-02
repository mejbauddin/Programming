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