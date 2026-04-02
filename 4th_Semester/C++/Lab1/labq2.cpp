#include <iostream>
using namespace std;

int main() {
    int n1, n2;
    cin >> n1 >> n2;
     
    if (n1 > n2) {
        int temp = n1;
        n1 = n2;
        n2 = temp;
    }
    
    int count = 0;
    
    for (int num = n1; num <= n2; num++) {
        if (num <= 1) continue; // Skip 1 and negative numbers
        
        int sum = 0;
        
        // Find all divisors (excluding the number itself)
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                sum = sum + i;
            }
        }
        
        // If sum of divisors equals the number, it's perfect
        if (sum == num) {
            count++;
        }
    }
    
    cout << count << endl;
    
    return 0;
}