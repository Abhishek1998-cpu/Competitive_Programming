#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T > 0)
    {
        int X;
        cin >> X;
        int sum = 0;
        while (X != 0)
        {
            sum = sum + X % 10;
            X = X / 10;
        }
        cout << sum << endl;

        T--;
    }
    return 0;
}