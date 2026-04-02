#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int result = 0;
    for (int i = n; i <= 10000; i++) {
        if (i % n == 0) {
            result = i;
        }
    }
    
    cout << result;
    return 0;
}

