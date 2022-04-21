// This is the solution of the "Strings" problem of Hackerank
#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    int temp = a[0];
    cout << a.size() << " " << b.size() << endl; //We can use .size or .length for finding the length of the string
    cout << a << b << endl;
    a[0] = b[0];
    b[0] = temp; // We can use this temp for swaping or we can also use inbuilt swap(x,y) function for swaping
    // swap(a[0], b[0]);
    cout << a << " " << b << endl;
    return 0;
}