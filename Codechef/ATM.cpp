#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    // your code goes here
    int X;
    float Y;
    cin >> X >> Y;
    if (X % 5 == 0 && X + 0.5 <= Y)
    {
        Y = Y - (X + 0.5);
        cout << Y;
    }
    else
    {
        cout << Y;
    }
    return 0;
}