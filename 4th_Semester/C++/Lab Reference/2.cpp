#include <iostream>
using namespace std;

bool is_divisible(int a, int b, int &q) {
    if (a % b == 0) {
        q = a / b;
        return true;
    } else {
        q = a / b;
        return false;
    }
}

int main() {
    int a, b, quotient;
    cin >> a >> b;
    
    if (is_divisible(a, b, quotient)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    cout << quotient << endl;
    
    return 0;
}