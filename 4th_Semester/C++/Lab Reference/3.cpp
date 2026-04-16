#include <iostream>
using namespace std;

bool is_divisible(int a, int b, int &q);

int main() {
    int a, b, q;

    cout << "Enter a and b: ";
    cin >> a >> b;

    bool result = is_divisible(a, b, q);

    if (result) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    cout << "quotient: " << q << endl;

    return 0;
}

bool is_divisible(int a, int b, int &q) {
    q = a / b;

    return (a % b == 0);
}