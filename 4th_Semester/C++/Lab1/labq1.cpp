// 题目：The largest divisible number

// 描述：
// Input an integer n greater than 0, find the largest integer within 10000 that can be divided by n, and output this integer.



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

