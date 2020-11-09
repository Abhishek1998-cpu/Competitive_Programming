// In this program we will try to understand .empty() function which is used to check certain container is empty or not
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string X = "";
    if (X.empty())
    {
        cout << "The string is empty" << endl;
    }
    else
    {
        cout << "The string is not empty" << endl;
    }

    cout << X.empty(); // string.empty() will return 1 or true if the string is empty and 0 or false if the string is not empty

    return 0;
}