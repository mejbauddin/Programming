#include <iostream>
using namespace std;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void sort_three(int &a, int &b, int &c) {
    
    if (a > b){
        swap(a,b);
    }
    if (a > c){
         swap(a,c);
    }
    if (b > c){
         swap(b,c);
    }
}


int main() {
    int x, y, z;
    cout << "Enter three integers: ";
    cin >> x >> y >> z;

    sort_three(x, y, z);

    cout << "Sorted: " << x << " " << y << " " << z << endl;
    return 0;
}
